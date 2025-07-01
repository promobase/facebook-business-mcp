"""
Code generation script to convert Facebook Business SDK AdObject fields to Pydantic models.

This script traverses all AdObject classes in the Facebook Business SDK and generates
corresponding Pydantic models with proper type annotations for use in MCP tools.
"""

import ast
import importlib
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

# Map Facebook SDK types to Python/Pydantic types
TYPE_MAPPING = {
    "string": "str",
    "unsigned int": "int",
    "int": "int",
    "float": "float",
    "bool": "bool",
    "datetime": "datetime",
    "list<string>": "list[str]",
    "list<int>": "list[int]",
    "list<float>": "list[float]",
    "list<bool>": "list[bool]",
    "map<string, int>": "dict[str, int]",
    "map<string, string>": "dict[str, str]",
    "map<string, float>": "dict[str, float]",
    "map<string, bool>": "dict[str, bool]",
    # Complex types - will be checked dynamically
    "list<AttributionSpec>": "list[dict[str, Any]]",
    "list<DeliveryCheck>": "list[dict[str, Any]]",
    "AgencyClientDeclaration": "dict[str, Any]",
    "FundingSourceDetails": "dict[str, Any]",
    "ExtendedCreditInvoiceGroup": "dict[str, Any]",
    "Business": "dict[str, Any]",
    "CRMAddress": "dict[str, Any]",
    "ReachFrequencySpec": "dict[str, Any]",
}


@dataclass
class FieldInfo:
    """Information about a field."""

    name: str
    python_name: str
    field_type: str
    python_type: str
    is_optional: bool = True


@dataclass
class EnumInfo:
    """Information about an enum class."""

    name: str
    values: list[tuple[str, str]]  # (python_name, value)


@dataclass
class ApiMethodInfo:
    """Information about an API method."""

    name: str
    http_method: str  # GET, POST, DELETE
    endpoint: Optional[str]  # e.g., "/ads"
    target_class: Optional[str]  # e.g., "Ad"
    param_types: dict[str, str]
    enums: dict[str, str]
    is_edge: bool = True  # Most methods are edge calls
    returns_iterator: bool = True  # GET methods usually return iterators


@dataclass
class AdObjectInfo:
    """Information about an AdObject."""

    name: str
    module_path: str
    fields: list[FieldInfo]
    enums: list[EnumInfo]
    field_types: dict[str, str]
    api_methods: Optional[list[ApiMethodInfo]] = None  # Will store API method info


class FacebookSDKParser:
    """Parser for Facebook Business SDK AdObject classes."""

    def __init__(self):
        # Use importlib to find the facebook_business module
        fb_module = importlib.import_module("facebook_business")
        fb_path = Path(fb_module.__file__).parent
        self.adobjects_path = fb_path / "adobjects"
        # Cache for discovered adobject types
        self._adobject_types = None
        self._discover_adobject_types()

    def _discover_adobject_types(self):
        """Discover all available AdObject types in the SDK."""
        self._adobject_types = {}
        for file_path in self.adobjects_path.glob("*.py"):
            if file_path.name.startswith("__"):
                continue

            # Parse the file to get the main class name
            with open(file_path) as f:
                try:
                    tree = ast.parse(f.read())
                    for node in ast.walk(tree):
                        if isinstance(node, ast.ClassDef) and self._is_adobject_class(node):
                            # Store mapping from class name to file stem
                            self._adobject_types[node.name] = file_path.stem
                            break
                except:
                    continue

    def find_adobject_files(self) -> list[Path]:
        """Find all Python files in the adobjects directory."""
        return list(self.adobjects_path.glob("*.py"))

    def parse_file(self, file_path: Path) -> Optional[AdObjectInfo]:
        """Parse a single Python file to extract AdObject information."""
        with open(file_path) as f:
            try:
                tree = ast.parse(f.read())
            except SyntaxError:
                print(f"Failed to parse {file_path}")
                return None

        # Find the main class that inherits from AbstractCrudObject or similar
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                # Check if it's an AdObject class
                if self._is_adobject_class(node):
                    return self._extract_adobject_info(node, file_path)

        return None

    def _is_adobject_class(self, node: ast.ClassDef) -> bool:
        """Check if a class is an AdObject (inherits from AbstractCrudObject or similar)."""
        for base in node.bases:
            if isinstance(base, ast.Name):
                if "Object" in base.id or "Mixin" in base.id:
                    return True
        return False

    def _extract_adobject_info(self, class_node: ast.ClassDef, file_path: Path) -> AdObjectInfo:
        """Extract information from an AdObject class."""
        fields = []
        enums = []
        field_types = {}
        api_methods = []

        # Find Field class
        field_class = self._find_inner_class(class_node, "Field")
        if field_class:
            fields = self._extract_fields(field_class)

        # Find enum classes (Currency, Tasks, etc.)
        for node in class_node.body:
            if isinstance(node, ast.ClassDef) and node.name != "Field":
                enum_info = self._extract_enum(node)
                if enum_info:
                    enums.append(enum_info)

        # Find _field_types assignment
        for node in class_node.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "_field_types":
                        field_types = self._extract_field_types(node.value)

        # Find API methods with param_types
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef):
                method_info = self._extract_api_method_info(node)
                if method_info:
                    api_methods.append(method_info)

        return AdObjectInfo(
            name=class_node.name,
            module_path=file_path.stem,
            fields=fields,
            enums=enums,
            field_types=field_types,
            api_methods=api_methods,
        )

    def _find_inner_class(self, class_node: ast.ClassDef, name: str) -> Optional[ast.ClassDef]:
        """Find an inner class by name."""
        for node in class_node.body:
            if isinstance(node, ast.ClassDef) and node.name == name:
                return node
        return None

    def _extract_fields(self, field_class: ast.ClassDef) -> list[FieldInfo]:
        """Extract field definitions from Field class."""
        # Python reserved keywords
        RESERVED_KEYWORDS = {
            "and",
            "as",
            "assert",
            "async",
            "await",
            "break",
            "class",
            "continue",
            "def",
            "del",
            "elif",
            "else",
            "except",
            "finally",
            "for",
            "from",
            "global",
            "if",
            "import",
            "in",
            "is",
            "lambda",
            "nonlocal",
            "not",
            "or",
            "pass",
            "raise",
            "return",
            "try",
            "while",
            "with",
            "yield",
            "True",
            "False",
            "None",
        }

        fields = []
        for node in field_class.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        field_name = target.id
                        if isinstance(node.value, ast.Constant):
                            field_value = node.value.value
                            # Handle reserved keywords
                            python_name = field_name
                            if field_value in RESERVED_KEYWORDS:
                                python_name = f"field_{field_value}"
                            fields.append(
                                FieldInfo(
                                    name=field_value,
                                    python_name=python_name,
                                    field_type="string",  # Default, will be overridden
                                    python_type="str",
                                )
                            )
        return fields

    def _extract_enum(self, enum_class: ast.ClassDef) -> Optional[EnumInfo]:
        """Extract enum values from an enum class."""
        values = []
        for node in enum_class.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        name = target.id
                        if isinstance(node.value, ast.Constant):
                            value = node.value.value
                            values.append((name, value))

        if values:
            return EnumInfo(name=enum_class.name, values=values)
        return None

    def _extract_field_types(self, dict_node: ast.Dict) -> dict[str, str]:
        """Extract field types from _field_types dictionary."""
        field_types = {}
        for key, value in zip(dict_node.keys, dict_node.values, strict=False):
            if isinstance(key, ast.Constant) and isinstance(value, ast.Constant):
                field_types[key.value] = value.value
        return field_types

    def _extract_api_method_info(self, func_node: ast.FunctionDef) -> Optional[ApiMethodInfo]:
        """Extract parameter types from API methods like get_ad_sets."""
        # Skip methods that don't match our pattern
        if not (func_node.name.startswith(("get_", "create_", "delete_"))):
            return None

        method_info = ApiMethodInfo(
            name=func_node.name,
            http_method="GET"
            if func_node.name.startswith("get_")
            else "POST"
            if func_node.name.startswith("create_")
            else "DELETE",
            endpoint=None,
            target_class=None,
            param_types={},
            enums={},
        )

        # Look for various assignments in the function body
        for node in ast.walk(func_node):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        if target.id == "param_types" and isinstance(node.value, ast.Dict):
                            method_info.param_types = self._extract_param_types(node.value)
                        elif target.id == "enums" and isinstance(node.value, ast.Dict):
                            method_info.enums = self._extract_enum_refs(node.value)

            # Look for FacebookRequest instantiation to get endpoint and target class
            elif (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == "FacebookRequest"
            ):
                for keyword in node.keywords:
                    if keyword.arg == "endpoint" and isinstance(keyword.value, ast.Constant):
                        method_info.endpoint = keyword.value.value
                    elif keyword.arg == "target_class" and isinstance(keyword.value, ast.Name):
                        method_info.target_class = keyword.value.id
                    elif keyword.arg == "method" and isinstance(keyword.value, ast.Constant):
                        method_info.http_method = keyword.value.value

            # Check for imports to get target class
            elif isinstance(node, ast.ImportFrom):
                # Extract class name from import like "from facebook_business.adobjects.ad import Ad"
                if node.module and "adobjects" in node.module:
                    for alias in node.names:
                        if hasattr(alias, "name"):
                            # This might be our target class
                            pass

        # Only return if we found param_types or it's a simple method
        if method_info.param_types or method_info.name in ["api_get", "api_update", "api_delete"]:
            return method_info
        return None

    def _extract_param_types(self, dict_node: ast.Dict) -> dict[str, str]:
        """Extract parameter types from param_types dictionary."""
        param_types = {}
        for key, value in zip(dict_node.keys, dict_node.values, strict=False):
            if isinstance(key, ast.Constant):
                param_name = key.value
                if isinstance(value, ast.Constant):
                    param_types[param_name] = value.value
        return param_types

    def _extract_enum_refs(self, dict_node: ast.Dict) -> dict[str, str]:
        """Extract enum references from enums dictionary."""
        enum_refs = {}
        for key, value in zip(dict_node.keys, dict_node.values, strict=False):
            if isinstance(key, ast.Constant):
                enum_name = key.value
                # Extract the enum class reference (e.g., Campaign.DatePreset)
                if isinstance(value, ast.Call):
                    # Handle values() call: Campaign.DatePreset.__dict__.values()
                    if isinstance(value.func, ast.Attribute) and value.func.attr == "values":
                        # Get the __dict__ attribute access
                        if (
                            isinstance(value.func.value, ast.Attribute)
                            and value.func.value.attr == "__dict__"
                        ):
                            # Get the enum class (e.g., Campaign.DatePreset)
                            if isinstance(value.func.value.value, ast.Attribute):
                                class_node = value.func.value.value
                                if isinstance(class_node.value, ast.Name):
                                    enum_refs[enum_name] = (
                                        f"{class_node.value.id}.{class_node.attr}"
                                    )
        return enum_refs


class PydanticModelGenerator:
    """Generator for Pydantic models from AdObject information."""

    def __init__(self, parser: FacebookSDKParser):
        self.imports: set[str] = set()
        self.type_checking_imports: set[str] = set()
        self.parser = parser

    def generate_model(self, adobject_info: AdObjectInfo) -> str:
        """Generate a Pydantic model for an AdObject."""
        self.imports.clear()
        self.type_checking_imports.clear()
        self.current_module = adobject_info.module_path
        # Standard library imports first
        self.imports.add("from __future__ import annotations")
        self.imports.add("from datetime import datetime")
        self.imports.add("from enum import Enum")
        self.imports.add("from typing import Any, Literal, TYPE_CHECKING")
        # Third party imports
        self.imports.add("from pydantic import BaseModel, ConfigDict, Field")

        model_parts = []

        # Generate enums
        for enum_info in adobject_info.enums:
            model_parts.append(self._generate_enum(adobject_info.name, enum_info))

        # Generate field model only (not the main model)
        model_parts.append(self._generate_field_model(adobject_info))

        # Generate parameter models for API methods
        if adobject_info.api_methods:
            for method_info in adobject_info.api_methods:
                param_model = self._generate_param_model(adobject_info.name, method_info)
                if param_model:
                    model_parts.append(param_model)

        # Combine imports and models with proper sorting
        # Separate imports into categories
        future_imports = []
        stdlib_imports = []
        third_party_imports = []
        local_imports = []

        for imp in self.imports:
            if "from __future__" in imp:
                future_imports.append(imp)
            elif any(
                imp.startswith(f"from {lib}") or imp.startswith(f"import {lib}")
                for lib in ["datetime", "enum", "typing"]
            ):
                stdlib_imports.append(imp)
            elif imp.startswith("from ."):
                local_imports.append(imp)
            else:
                third_party_imports.append(imp)

        # Build imports section with proper ordering
        imports_sections = []
        if future_imports:
            imports_sections.append("\n".join(sorted(future_imports)))
        if stdlib_imports:
            imports_sections.append("\n".join(sorted(stdlib_imports)))
        if third_party_imports:
            imports_sections.append("\n".join(sorted(third_party_imports)))
        if local_imports:
            imports_sections.append("\n".join(sorted(local_imports)))

        # Add TYPE_CHECKING imports if any
        if self.type_checking_imports:
            # Filter out any TYPE_CHECKING imports that are already in regular imports
            all_regular_imports = "\n".join(imports_sections)
            filtered_type_checking = []
            for imp in sorted(self.type_checking_imports):
                # Extract the import content after "from .module import "
                import_parts = imp.split(" import ")
                if len(import_parts) == 2:
                    module_part, items_part = import_parts
                    # Check if these specific items are already imported from the same module
                    if f"{module_part} import" not in all_regular_imports:
                        filtered_type_checking.append(imp)
                    else:
                        # Check each individual item
                        items = [item.strip() for item in items_part.split(",")]
                        missing_items = []
                        for item in items:
                            if item not in all_regular_imports:
                                missing_items.append(item)
                        if missing_items:
                            filtered_type_checking.append(
                                f"{module_part} import {', '.join(missing_items)}"
                            )

            if filtered_type_checking:
                type_checking_section = ["", "if TYPE_CHECKING:"]
                for imp in filtered_type_checking:
                    type_checking_section.append(f"    {imp}")
                imports_sections.append("\n".join(type_checking_section))

        imports_str = "\n\n".join(imports_sections)
        models_str = "\n\n".join(model_parts)

        # Add header comment
        header = '"""Code generated by PromoBase script - DO NOT EDIT MANUALLY."""\n\n'

        return f"{header}{imports_str}\n\n\n{models_str}"

    def _generate_enum(self, class_name: str, enum_info: EnumInfo) -> str:
        """Generate an Enum class."""
        enum_name = f"{class_name}{enum_info.name}"
        lines = [f"class {enum_name}(str, Enum):"]
        lines.append(f'    """Enum for {class_name}.{enum_info.name}."""')

        for python_name, value in enum_info.values:
            # Handle special cases
            if python_name == "value_try":  # Special case for 'try' keyword
                python_name = "try_"
            lines.append(f'    {python_name.upper()} = "{value}"')

        return "\n".join(lines)

    def _generate_field_model(self, adobject_info: AdObjectInfo) -> str:
        """Generate the fields model."""
        lines = []

        # Generate the Literal type for fields
        field_literals = [f'"{field.name}"' for field in adobject_info.fields]
        if field_literals:
            # Split into multiple lines if there are many fields
            if len(field_literals) > 5:
                lines.append(f"{adobject_info.name}Field = Literal[")
                for i, literal in enumerate(field_literals):
                    comma = "," if i < len(field_literals) - 1 else ""
                    lines.append(f"    {literal}{comma}")
                lines.append("]")
            else:
                literals_str = ", ".join(field_literals)
                lines.append(f"{adobject_info.name}Field = Literal[{literals_str}]")
        else:
            lines.append(f"{adobject_info.name}Field = Literal['']  # No fields defined")

        lines.append("")
        lines.append("")

        # Then generate the Pydantic model
        lines.append(f"class {adobject_info.name}Fields(BaseModel):")
        lines.append(f'    """Pydantic model for {adobject_info.name} fields."""')
        lines.append("")

        # Update field types based on _field_types
        field_map = {field.name: field for field in adobject_info.fields}

        for field_name, field_type in adobject_info.field_types.items():
            if field_name in field_map:
                field = field_map[field_name]
                python_type = self._map_field_type(field_type)

                # Make all fields optional by default
                python_type = f"{python_type} | None"

                field_def = (
                    f'    {field.python_name}: {python_type} = Field(None, alias="{field.name}")'
                )
                lines.append(field_def)

        lines.append("")
        lines.append("    model_config = ConfigDict(")
        lines.append("        populate_by_alias=True,")
        lines.append("        extra='forbid'")
        lines.append("    )")

        return "\n".join(lines)

    def _map_field_type(self, field_type: str) -> str:
        """Map Facebook SDK field type to Python type."""
        # Direct mapping
        if field_type in TYPE_MAPPING:
            return TYPE_MAPPING[field_type]

        # Check if this is an adobject type
        if field_type in self.parser._adobject_types:
            # Import the fields model from the corresponding module
            module_name = self.parser._adobject_types[field_type]
            fields_model = f"{field_type}Fields"
            # Check if it's a self-reference
            if module_name != self.current_module:
                self.type_checking_imports.add(f"from .{module_name} import {fields_model}")
            # Don't use string annotation since we have from __future__ import annotations
            return fields_model

        # Handle list types
        if field_type.startswith("list<") and field_type.endswith(">"):
            inner_type = field_type[5:-1]
            mapped_inner = self._map_field_type(inner_type)
            return f"list[{mapped_inner}]"

        # Handle map types
        if field_type.startswith("map<") and field_type.endswith(">"):
            parts = field_type[4:-1].split(",", 1)
            if len(parts) == 2:
                key_type = self._map_field_type(parts[0].strip())
                value_type = self._map_field_type(parts[1].strip())
                return f"dict[{key_type}, {value_type}]"

        # Default to Any for unknown types
        return "dict[str, Any]"

    def _generate_param_model(self, class_name: str, method_info: ApiMethodInfo) -> Optional[str]:
        """Generate a Pydantic model for API method parameters."""
        if not method_info.param_types:
            return None

        # Python reserved keywords
        RESERVED_KEYWORDS = {
            "and",
            "as",
            "assert",
            "async",
            "await",
            "break",
            "class",
            "continue",
            "def",
            "del",
            "elif",
            "else",
            "except",
            "finally",
            "for",
            "from",
            "global",
            "if",
            "import",
            "in",
            "is",
            "lambda",
            "nonlocal",
            "not",
            "or",
            "pass",
            "raise",
            "return",
            "try",
            "while",
            "with",
            "yield",
            "True",
            "False",
            "None",
        }

        lines = []
        method_name = method_info.name
        # Convert method name to PascalCase for the model name
        model_name = (
            f"{class_name}{''.join(word.capitalize() for word in method_name.split('_'))}Params"
        )

        lines.append(f"class {model_name}(BaseModel):")
        lines.append(f'    """Parameters for {class_name}.{method_name}()."""')
        lines.append("")

        # Track enum imports needed for this model
        local_enum_imports = set()

        # Generate fields for each parameter
        for param_name, param_type in method_info.param_types.items():
            python_type = self._map_param_type(param_type, method_info.enums)
            # Track if we need to add enum imports
            if param_type.endswith("_enum") and param_type in method_info.enums:
                enum_ref = method_info.enums[param_type]
                if "." in enum_ref:
                    class_name_ref, enum_name = enum_ref.rsplit(".", 1)
                    full_enum_name = f"{class_name_ref}{enum_name}"
                    # Check if it's from a different module
                    if class_name_ref in self.parser._adobject_types:
                        module_name = self.parser._adobject_types[class_name_ref]
                        if module_name != self.current_module:
                            local_enum_imports.add((module_name, full_enum_name))

            # Make all params optional by default
            field_name = param_name
            if param_name in RESERVED_KEYWORDS:
                field_name = f"field_{param_name}"
                field_def = f'    {field_name}: {python_type} | None = Field(None, alias="{param_name}", description="{param_name} parameter")'
            else:
                field_def = f'    {param_name}: {python_type} | None = Field(None, description="{param_name} parameter")'
            lines.append(field_def)

        lines.append("")
        lines.append("    model_config = ConfigDict(extra='forbid')")

        # Add the enum imports to the general imports (not TYPE_CHECKING)
        for module_name, enum_name in local_enum_imports:
            self.imports.add(f"from .{module_name} import {enum_name}")

        return "\n".join(lines)

    def _map_param_type(self, param_type: str, enums: dict) -> str:
        """Map Facebook SDK parameter type to Python type."""
        # Handle enum types
        if param_type.endswith("_enum"):
            # Check if we have the enum reference
            if param_type in enums:
                enum_ref = enums[param_type]
                # Extract the enum name (e.g., "Campaign.DatePreset")
                if "." in enum_ref:
                    class_name, enum_name = enum_ref.rsplit(".", 1)
                    # Import the enum from the appropriate module
                    module_name = class_name.lower()
                    if class_name in self.parser._adobject_types:
                        module_name = self.parser._adobject_types[class_name]
                    # Add to regular imports (not TYPE_CHECKING) since enums are runtime values
                    if module_name != self.current_module:
                        self.imports.add(f"from .{module_name} import {class_name}{enum_name}")
                    # Return the properly typed enum reference
                    return f"{class_name}{enum_name}"  # No string annotation needed with __future__ annotations
            return "str"

        # Check if this is an adobject type
        if param_type in self.parser._adobject_types:
            # Import the fields model from the corresponding module
            module_name = self.parser._adobject_types[param_type]
            fields_model = f"{param_type}Fields"
            # Check if it's a self-reference
            if module_name != self.current_module:
                self.type_checking_imports.add(f"from .{module_name} import {fields_model}")
            # Don't use string annotation since we have from __future__ import annotations
            return fields_model

        # Handle list types
        if param_type.startswith("list<") and param_type.endswith(">"):
            inner_type = param_type[5:-1]
            mapped_inner = self._map_param_type(inner_type, enums)
            return f"list[{mapped_inner}]"

        # Basic type mappings
        type_map = {
            "bool": "bool",
            "int": "int",
            "string": "str",
            "map": "dict[str, Any]",
            "datetime": "datetime",
            "unsigned int": "int",
            "float": "float",
        }

        return type_map.get(param_type, "Any")


def generate_comprehensive_types_file(output_dir: Path):
    """Generate a comprehensive file with all field types and models."""
    lines = []
    lines.append('"""Code generated by PromoBase script - DO NOT EDIT MANUALLY."""')
    lines.append("")
    lines.append("from __future__ import annotations")
    lines.append("")
    lines.append('"""Comprehensive type definitions for Facebook Marketing API objects."""')
    lines.append("")
    lines.append("from typing import Union")
    lines.append("")

    # Process all generated model files (excluding special files)
    module_files = []
    for f in sorted(output_dir.glob("*.py")):
        if not f.stem.startswith("__") and f.stem not in ["fb_types", "types", "init"]:
            module_files.append(f)

    # Collect all field literals and models
    field_literals = []
    field_models = []
    param_models = []

    for module_file in module_files:
        module_name = module_file.stem
        class_name = "".join(word.capitalize() for word in module_name.split("_"))

        # Import field literal
        field_literal = f"{class_name}Field"
        field_literals.append((module_name, field_literal))

        # Import fields model
        fields_model = f"{class_name}Fields"
        field_models.append((module_name, fields_model))

        # Import all param models (we'll need to parse the file to find these)
        with open(module_file) as f:
            content = f.read()
            import re

            # Find all classes that end with Params
            param_classes = re.findall(r"class (\w+Params)\(BaseModel\):", content)
            for param_class in param_classes:
                param_models.append((module_name, param_class))

    # Generate imports
    for module_name, field_literal in field_literals:
        lines.append(f"from .{module_name} import {field_literal}")
    lines.append("")

    for module_name, fields_model in field_models:
        lines.append(f"from .{module_name} import {fields_model}")
    lines.append("")

    # Import param models
    imported_modules = set()
    for module_name, param_model in param_models:
        if module_name not in imported_modules:
            # Get all param models from this module
            module_params = [pm for mn, pm in param_models if mn == module_name]
            if len(module_params) <= 3:
                lines.append(f"from .{module_name} import {', '.join(module_params)}")
            else:
                lines.append(f"from .{module_name} import (")
                for i, param in enumerate(module_params):
                    comma = "," if i < len(module_params) - 1 else ""
                    lines.append(f"    {param}{comma}")
                lines.append(")")
            imported_modules.add(module_name)
    lines.append("")

    # Create union types
    lines.append("# Union types for field literals")
    lines.append("AnyField = Union[")
    for i, (_, field_literal) in enumerate(field_literals):
        comma = "," if i < len(field_literals) - 1 else ""
        lines.append(f"    {field_literal}{comma}")
    lines.append("]")
    lines.append("")

    lines.append("# Union types for field models")
    lines.append("AnyFieldModel = Union[")
    for i, (_, fields_model) in enumerate(field_models):
        comma = "," if i < len(field_models) - 1 else ""
        lines.append(f"    {fields_model}{comma}")
    lines.append("]")
    lines.append("")

    lines.append("# Export all types")
    lines.append("__all__ = [")
    lines.append('    "AnyField",')
    lines.append('    "AnyFieldModel",')

    for _, field_literal in field_literals:
        lines.append(f'    "{field_literal}",')

    for _, fields_model in field_models:
        lines.append(f'    "{fields_model}",')

    for _, param_model in param_models:
        lines.append(f'    "{param_model}",')

    lines.append("]")

    # Write the file
    types_file = output_dir / "fb_types.py"
    with open(types_file, "w") as f:
        f.write("\n".join(lines))

    print(f"  Generated {types_file}")


def main():
    """Main function to generate Pydantic models."""
    parser = FacebookSDKParser()
    generator = PydanticModelGenerator(parser)

    # Output directories
    models_dir = Path("src/generated/models")
    models_dir.mkdir(parents=True, exist_ok=True)

    wrappers_dir = Path("src/generated/wrappers")
    wrappers_dir.mkdir(parents=True, exist_ok=True)

    # Clean up existing files first
    print("Cleaning up existing generated files...")
    # Remove old _models.py files
    for old_file in models_dir.glob("*_models.py"):
        old_file.unlink()
        print(f"  Removed {old_file}")
    # Remove new .py files (excluding special files)
    for old_file in models_dir.glob("*.py"):
        if not old_file.stem.startswith("__") and old_file.stem not in ["fb_types"]:
            old_file.unlink()
            print(f"  Removed {old_file}")

    # Process all AdObject files
    adobject_files = parser.find_adobject_files()

    # Filter out non-adobject files (like __init__.py, abstractobject.py, etc.)
    files_to_process = []
    for file_path in adobject_files:
        # Skip special files
        if file_path.stem.startswith("__") or file_path.stem in [
            "abstractobject",
            "abstractcrudobject",
            "apispecfile",
        ]:
            continue
        files_to_process.append(file_path)

    print(f"\nFound {len(files_to_process)} ad object files to process")

    generated_files = []
    for file_path in files_to_process:
        print(f"\nProcessing {file_path.name}...")
        adobject_info = parser.parse_file(file_path)

        if adobject_info and adobject_info.fields:
            # Generate Pydantic model
            model_code = generator.generate_model(adobject_info)

            # Write to file
            output_file = models_dir / f"{adobject_info.module_path}.py"
            with open(output_file, "w") as f:
                f.write(model_code)

            generated_files.append(output_file)
            print(f"  ✓ Generated {output_file}")
            print(f"    - {len(adobject_info.fields)} fields")
            print(f"    - {len(adobject_info.enums)} enums")
            print(f"    - {len(adobject_info.api_methods)} API methods with params")
        else:
            print(f"  ✗ No fields found in {file_path.name}")

    # Generate __init__.py for all models
    init_file = models_dir / "__init__.py"
    with open(init_file, "w") as f:
        f.write('"""Code generated by PromoBase script - DO NOT EDIT MANUALLY."""\n')
        f.write('"""Auto-generated Pydantic models for Facebook Business SDK objects."""\n\n')
        # Include all generated model files
        for module_name in sorted([f.stem for f in generated_files]):
            f.write(f"from .{module_name} import *  # noqa: F403\n")

    print("\n✓ Generated __init__.py")

    # Generate a comprehensive types file that exports all field literals
    print("\nGenerating comprehensive types file...")
    generate_comprehensive_types_file(models_dir)

    print(f"\n✓ Successfully generated {len(generated_files)} model files in {models_dir}")

    # Ruff formatting will be done by the main codegen.py script


if __name__ == "__main__":
    main()
