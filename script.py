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
    # Complex types - we'll use Any for now
    "list<AttributionSpec>": "list[dict[str, Any]]",
    "list<DeliveryCheck>": "list[dict[str, Any]]",
    "AgencyClientDeclaration": "dict[str, Any]",
    "AdAccountPromotableObjects": "dict[str, Any]",
    "CustomAudienceGroup": "dict[str, Any]",
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
class AdObjectInfo:
    """Information about an AdObject."""

    name: str
    module_path: str
    fields: list[FieldInfo]
    enums: list[EnumInfo]
    field_types: dict[str, str]
    api_methods: Optional[list[dict]] = None  # Will store API method info


class FacebookSDKParser:
    """Parser for Facebook Business SDK AdObject classes."""

    def __init__(self):
        # Use importlib to find the facebook_business module
        fb_module = importlib.import_module("facebook_business")
        fb_path = Path(fb_module.__file__).parent
        self.adobjects_path = fb_path / "adobjects"

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
        fields = []
        for node in field_class.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        field_name = target.id
                        if isinstance(node.value, ast.Constant):
                            field_value = node.value.value
                            fields.append(
                                FieldInfo(
                                    name=field_value,
                                    python_name=field_name,
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

    def _extract_api_method_info(self, func_node: ast.FunctionDef) -> Optional[dict]:
        """Extract parameter types from API methods like get_ad_sets."""
        method_info = {
            "name": func_node.name,
            "param_types": {},
            "enums": {},
        }

        # Look for param_types dictionary in the function body
        for node in ast.walk(func_node):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "param_types":
                        if isinstance(node.value, ast.Dict):
                            method_info["param_types"] = self._extract_param_types(node.value)
                    elif isinstance(target, ast.Name) and target.id == "enums":
                        if isinstance(node.value, ast.Dict):
                            method_info["enums"] = self._extract_enum_refs(node.value)

        # Only return if we found param_types
        if method_info["param_types"]:
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
                # Extract the enum class reference (e.g., AdSet.DatePreset)
                if isinstance(value, ast.Attribute):
                    if isinstance(value.value, ast.Attribute) and isinstance(
                        value.value.value, ast.Name
                    ):
                        enum_refs[enum_name] = f"{value.value.value.id}.{value.value.attr}"
        return enum_refs


class PydanticModelGenerator:
    """Generator for Pydantic models from AdObject information."""

    def __init__(self):
        self.imports: set[str] = set()

    def generate_model(self, adobject_info: AdObjectInfo) -> str:
        """Generate a Pydantic model for an AdObject."""
        self.imports.clear()
        # Standard library imports first
        self.imports.add("from __future__ import annotations")
        self.imports.add("from datetime import datetime")
        self.imports.add("from enum import Enum")
        self.imports.add("from typing import Any, Literal")
        # Third party imports
        self.imports.add("from pydantic import BaseModel, Field")

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

        for imp in self.imports:
            if "from __future__" in imp:
                future_imports.append(imp)
            elif any(
                imp.startswith(f"from {lib}") or imp.startswith(f"import {lib}")
                for lib in ["datetime", "enum", "typing"]
            ):
                stdlib_imports.append(imp)
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
        lines.append("    class Config:")
        lines.append("        populate_by_name = True")
        lines.append("        extra = 'forbid'")

        return "\n".join(lines)

    def _map_field_type(self, field_type: str) -> str:
        """Map Facebook SDK field type to Python type."""
        # Direct mapping
        if field_type in TYPE_MAPPING:
            return TYPE_MAPPING[field_type]

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

    def _generate_param_model(self, class_name: str, method_info: dict) -> Optional[str]:
        """Generate a Pydantic model for API method parameters."""
        if not method_info["param_types"]:
            return None

        lines = []
        method_name = method_info["name"]
        # Convert method name to PascalCase for the model name
        model_name = (
            f"{class_name}{''.join(word.capitalize() for word in method_name.split('_'))}Params"
        )

        lines.append(f"class {model_name}(BaseModel):")
        lines.append(f'    """Parameters for {class_name}.{method_name}()."""')
        lines.append("")

        # Generate fields for each parameter
        for param_name, param_type in method_info["param_types"].items():
            python_type = self._map_param_type(param_type, method_info["enums"])
            # Make all params optional by default
            field_def = f'    {param_name}: {python_type} | None = Field(None, description="{param_name} parameter")'
            lines.append(field_def)

        lines.append("")
        lines.append("    class Config:")
        lines.append("        extra = 'forbid'")

        return "\n".join(lines)

    def _map_param_type(self, param_type: str, enums: dict) -> str:
        """Map Facebook SDK parameter type to Python type."""
        # Handle enum types
        if param_type.endswith("_enum"):
            # Check if we have the enum reference
            if param_type in enums:
                enum_ref = enums[param_type]
                # Extract the enum name (e.g., "AdSet.DatePreset" -> "DatePreset")
                if "." in enum_ref:
                    _, enum_name = enum_ref.rsplit(".", 1)
                    # We'll use the enum from the same module if available
                    return "str"  # For now, use str; could be improved to use actual enum
            return "str"

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
    lines.append('"""Comprehensive type definitions for Facebook Marketing API core objects."""')
    lines.append("")
    lines.append("from __future__ import annotations")
    lines.append("")
    lines.append("from typing import Union")
    lines.append("")

    # Only process core model files
    core_objects = ["adaccount", "campaign", "adset", "ad", "adcreative", "customaudience"]
    module_files = []
    for obj in core_objects:
        model_file = output_dir / f"{obj}_models.py"
        if model_file.exists():
            module_files.append(model_file)

    module_files = sorted(module_files)

    # Collect all field literals and models
    field_literals = []
    field_models = []
    param_models = []

    for module_file in module_files:
        module_name = module_file.stem
        class_name = "".join(
            word.capitalize() for word in module_name.replace("_models", "").split("_")
        )

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
    types_file = output_dir / "types.py"
    with open(types_file, "w") as f:
        f.write("\n".join(lines))

    print(f"  Generated {types_file}")


def main():
    """Main function to generate Pydantic models."""
    parser = FacebookSDKParser()
    generator = PydanticModelGenerator()

    # Output directory
    output_dir = Path("src/generated/models")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Clean up existing files first (only for core objects)
    print("Cleaning up existing generated files...")
    core_objects = ["adaccount", "campaign", "adset", "ad", "adcreative", "customaudience"]
    for obj in core_objects:
        old_file = output_dir / f"{obj}_models.py"
        if old_file.exists():
            old_file.unlink()
            print(f"  Removed {old_file}")

    # Process only core AdObject files
    adobject_files = parser.find_adobject_files()

    # Filter to only core objects
    core_files = []
    for file_path in adobject_files:
        # Match exact filenames for core objects
        if file_path.stem in core_objects:
            core_files.append(file_path)

    print(f"\nFound {len(core_files)} core ad object files to process")

    generated_files = []
    for file_path in core_files:
        print(f"\nProcessing {file_path.name}...")
        adobject_info = parser.parse_file(file_path)

        if adobject_info and adobject_info.fields:
            # Generate Pydantic model
            model_code = generator.generate_model(adobject_info)

            # Write to file
            output_file = output_dir / f"{adobject_info.module_path}_models.py"
            with open(output_file, "w") as f:
                f.write(model_code)

            generated_files.append(output_file)
            print(f"  ✓ Generated {output_file}")
            print(f"    - {len(adobject_info.fields)} fields")
            print(f"    - {len(adobject_info.enums)} enums")
            print(f"    - {len(adobject_info.api_methods)} API methods with params")
        else:
            print(f"  ✗ No fields found in {file_path.name}")

    # Generate __init__.py only for core models
    init_file = output_dir / "__init__.py"
    with open(init_file, "w") as f:
        f.write('"""Code generated by PromoBase script - DO NOT EDIT MANUALLY."""\n')
        f.write('"""Auto-generated Pydantic models for Facebook Business SDK core objects."""\n\n')
        # Only include the core model files
        for module_name in sorted([f.stem for f in generated_files]):
            f.write(f"from .{module_name} import *  # noqa: F403\n")

    print("\n✓ Generated __init__.py")

    # Generate a comprehensive types file that exports all field literals
    print("\nGenerating comprehensive types file...")
    generate_comprehensive_types_file(output_dir)

    print(f"\n✓ Successfully generated {len(generated_files)} core model files in {output_dir}")


if __name__ == "__main__":
    main()
