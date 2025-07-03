"""
Unified generator that reads from API specs and generates:
1. Individual model files with field literals and param models
2. Comprehensive all_models.py file
3. Support for both SDK parsing and API spec parsing

This consolidates gen.py and generate_models.py functionality.
"""

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

from jinja2 import Template

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

# Pydantic BaseModel reserved attributes
PYDANTIC_RESERVED = {
    "schema",
    "model_config",
    "model_fields",
    "model_computed_fields",
    "model_extra",
    "model_fields_set",
}


@dataclass
class FieldInfo:
    """Information about a field."""

    name: str
    python_name: str
    field_type: str
    python_type: str
    required: bool = False
    description: str = ""


@dataclass
class EnumInfo:
    """Information about an enum."""

    name: str
    values: list[tuple[str, str]]  # (python_name, value)
    node: str = ""
    field_or_param: str = ""


@dataclass
class ApiMethodInfo:
    """Information about an API method."""

    method: str  # GET, POST, DELETE
    endpoint: str
    return_type: str
    params: list[dict[str, Any]]

    @property
    def method_name(self) -> str:
        """Generate method name from HTTP method and endpoint."""
        # Clean endpoint - remove leading slash if present
        endpoint = self.endpoint.lstrip("/")

        # Convert endpoint to SDK method name format by adding underscores
        # Examples: "adcreatives" -> "ad_creatives", "adcreativesbylabels" -> "ad_creatives_by_labels"
        endpoint_with_underscores = self._add_underscores_to_endpoint(endpoint)

        if self.method == "GET":
            return f"get_{endpoint_with_underscores}"
        elif self.method == "POST":
            # For POST, check if endpoint already suggests creation
            if endpoint_with_underscores.startswith("create_"):
                return endpoint_with_underscores
            # Remove plural for create methods
            return f"create_{endpoint_with_underscores.rstrip('s')}"
        elif self.method == "DELETE":
            return f"delete_{endpoint_with_underscores}"
        return f"{self.method.lower()}_{endpoint_with_underscores}"

    def _add_underscores_to_endpoint(self, endpoint: str) -> str:
        """Add underscores to convert API endpoint to SDK method name format.

        Examples:
        - "adcreatives" -> "ad_creatives"
        - "adcreativesbylabels" -> "ad_creatives_by_labels"
        - "asyncadcreatives" -> "async_ad_creatives"
        - "customaudiences" -> "custom_audiences"
        - "targetingsentencelines" -> "targeting_sentence_lines"
        - "adrulesgoverned" -> "ad_rules_governed"
        - "ads_reporting_mmm_schedulers" -> "ads_reporting_mmm_schedulers" (preserved)
        """
        result = endpoint.lower()

        # If endpoint already contains underscores, return as-is
        # This preserves endpoints like "ads_reporting_mmm_schedulers"
        if "_" in result:
            return result

        # Special cases that need specific handling
        special_cases = {
            "adcreatives": "ad_creatives",
            "adcreativesbylabels": "ad_creatives_by_labels",
            "asyncadcreatives": "async_ad_creatives",
            "customaudiences": "custom_audiences",
            "adrulesgoverned": "ad_rules_governed",
            "targetingsentencelines": "targeting_sentence_lines",
            "adaccounts": "ad_accounts",
            "adimages": "ad_images",
            "advideos": "ad_videos",
            "adsets": "ad_sets",
            "adlabels": "ad_labels",
            "adrules": "ad_rules",
            "adpixels": "ad_pixels",
            "asyncadrequests": "async_ad_requests",
            "asyncadsets": "async_ad_sets",
            "productcatalogs": "product_catalogs",
            "productfeeds": "product_feeds",
            "productsets": "product_sets",
            "productgroups": "product_groups",
            "productitems": "product_items",
        }

        # Check if it's a known special case
        if result in special_cases:
            return special_cases[result]

        # General patterns for other cases
        patterns = [
            # Handle async prefix
            (r"^(async)(.+)", r"\1_\2"),
            # Split "by" when it's between words
            (r"([a-z]+)by([a-z]+)", r"\1_by_\2"),
            # Handle common ad-prefixed patterns not in special cases
            (r"^(ad)([a-z]+)", r"\1_\2"),
            # Handle common product-prefixed patterns
            (r"^(product)([a-z]+)", r"\1_\2"),
            # Handle custom prefix
            (r"^(custom)([a-z]+)", r"\1_\2"),
            # Split compound words at known boundaries
            (r"(targeting)(sentence)", r"\1_\2"),
            (r"(sentence)(lines)", r"\1_\2"),
            (r"([a-z]+)(governed|based|matched)$", r"\1_\2"),
        ]

        for pattern, replacement in patterns:
            result = re.sub(pattern, replacement, result)

        # Clean up any double underscores
        result = re.sub(r"_+", "_", result)

        return result


@dataclass
class AdObjectSpec:
    """Complete specification for an AdObject."""

    name: str
    module_path: str  # lowercase name for module
    fields: list[FieldInfo]
    apis: list[ApiMethodInfo]
    enums: list[EnumInfo] = None

    def __post_init__(self):
        if self.enums is None:
            self.enums = []


def sanitize_field_name(field_name: str) -> str:
    """Sanitize field names to be valid Python identifiers."""
    # Replace dots and other invalid characters with underscores
    sanitized = re.sub(r"[^a-zA-Z0-9_]", "_", field_name)

    # If field name starts with a digit, prefix it with 'field_'
    if sanitized and sanitized[0].isdigit():
        sanitized = f"field_{sanitized}"

    # If field name is a reserved keyword, append underscore
    if sanitized in RESERVED_KEYWORDS:
        sanitized = f"{sanitized}_"

    # If field name conflicts with Pydantic reserved names, append underscore
    if sanitized in PYDANTIC_RESERVED:
        sanitized = f"{sanitized}_"

    # If the name becomes empty or just underscores, use a default
    if not sanitized or sanitized.replace("_", "") == "":
        sanitized = "field_unnamed"

    return sanitized


def sanitize_enum_member_name(value: str) -> str:
    """Sanitize enum member names to be valid Python identifiers."""
    # Replace invalid characters with underscores
    sanitized = re.sub(r"[^a-zA-Z0-9_]", "_", value)

    # If the name starts with a digit, prefix it with 'VALUE_'
    if sanitized and sanitized[0].isdigit():
        sanitized = f"VALUE_{sanitized}"

    # If the name is empty or just underscores, use a default
    if not sanitized or sanitized.replace("_", "") == "":
        sanitized = "VALUE_EMPTY"

    # Remove multiple consecutive underscores
    sanitized = re.sub(r"_+", "_", sanitized)

    # Remove trailing underscores
    sanitized = sanitized.rstrip("_")

    # If original value was simple (alphanumeric + underscore), keep it as is
    # Otherwise convert to uppercase
    if re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", value):
        return value
    else:
        return sanitized.upper()


def load_enum_types(enum_file: Path) -> dict[str, EnumInfo]:
    """Load enum definitions from enum_types.json."""
    enums = {}

    if not enum_file.exists():
        print(f"Warning: {enum_file} not found. No enums will be generated.")
        return enums

    with open(enum_file) as f:
        enum_data = json.load(f)

    for enum_def in enum_data:
        enum_name = enum_def["name"]
        values = []
        for value in enum_def["values"]:
            python_name = sanitize_enum_member_name(value)
            values.append((python_name, value))

        enums[enum_name] = EnumInfo(
            name=enum_name,
            values=values,
            node=enum_def.get("node", ""),
            field_or_param=enum_def.get("field_or_param", ""),
        )

    return enums


def parse_type_to_python(
    type_str: str,
    known_types: set[str] = None,
    is_param: bool = False,
    referenced_types: set[str] = None,
    enum_types: set[str] = None,
) -> str:
    """Convert API type to Python/Pydantic type hint.

    Args:
        type_str: The type string from the API spec
        known_types: Set of known AdObject types
        is_param: Whether this is for a parameter (vs field)
        referenced_types: Set to collect referenced types (for import generation)
        enum_types: Set to collect enum types used (for enum generation)
    """
    if not type_str:
        return "Any"

    # Basic type mappings
    type_mapping = {
        "string": "str",
        "int": "int",
        "unsigned int": "int",
        "bool": "bool",
        "datetime": "datetime",
        "map": "dict[str, Any]",
        "Object": "dict[str, Any]",
        "float": "float",
        "double": "float",
    }

    # Handle map types like map<string, int> or map<string, Business>
    if type_str.startswith("map<") and type_str.endswith(">"):
        inner_types = type_str[4:-1]  # Remove 'map<' and '>'
        if "," in inner_types:
            key_type, value_type = [t.strip() for t in inner_types.split(",", 1)]
            parsed_key = parse_type_to_python(
                key_type, known_types, is_param, referenced_types, enum_types
            )
            parsed_value = parse_type_to_python(
                value_type, known_types, is_param, referenced_types, enum_types
            )
            return f"dict[{parsed_key}, {parsed_value}]"
        else:
            # Single type map, assume string keys
            parsed_value = parse_type_to_python(
                inner_types, known_types, is_param, referenced_types, enum_types
            )
            return f"dict[str, {parsed_value}]"

    # Handle list types
    if type_str.startswith("list<") and type_str.endswith(">"):
        inner_type = type_str[5:-1]  # Remove 'list<' and '>'
        parsed_inner = parse_type_to_python(
            inner_type, known_types, is_param, referenced_types, enum_types
        )
        return f"list[{parsed_inner}]"

    # Handle enum parameter types - return the enum name itself, not str
    if "_enum_param" in type_str or type_str.endswith("_enum"):
        # Track this enum type if collecting
        if enum_types is not None:
            enum_types.add(type_str)
        # For params, return the enum type name
        return type_str

    # Basic type lookup
    if type_str in type_mapping:
        return type_mapping[type_str]

    # For fields referencing other AdObjects
    if known_types and type_str in known_types:
        if is_param:
            # For params, we need to track the reference and use the proper type
            if referenced_types is not None:
                referenced_types.add(type_str)
            # Return the actual type name for params - we'll handle imports properly
            return f"{type_str}Fields"
        else:
            # For fields, use the Fields model and track the reference
            if referenced_types is not None:
                referenced_types.add(type_str)
            return f"{type_str}Fields"

    # Default to dict for unknown complex types
    return "dict[str, Any]"


def load_spec_file(spec_file: Path, known_types: set[str]) -> Optional[AdObjectSpec]:
    """Load and parse a single spec file."""
    with open(spec_file) as f:
        spec_data = json.load(f)

    # Extract name from filename
    name = spec_file.stem
    module_path = name.lower()

    # Parse fields
    fields = []
    if "fields" in spec_data:
        for field_data in spec_data["fields"]:
            field_name = field_data["name"]
            field_type = field_data.get("type", "Any")
            python_name = sanitize_field_name(field_name)
            # Don't collect references here, we'll do it in generate_model_file
            python_type = parse_type_to_python(field_type, known_types, is_param=False)

            fields.append(
                FieldInfo(
                    name=field_name,
                    python_name=python_name,
                    field_type=field_type,
                    python_type=python_type,
                    description=field_data.get("description", ""),
                )
            )

    # Parse APIs
    apis = []
    if "apis" in spec_data:
        for api_data in spec_data["apis"]:
            # Skip if missing required fields
            if "method" not in api_data or "endpoint" not in api_data:
                continue

            apis.append(
                ApiMethodInfo(
                    method=api_data["method"],
                    endpoint=api_data["endpoint"],
                    return_type=api_data.get("return", "Any"),
                    params=api_data.get("params", []),
                )
            )

    return AdObjectSpec(name=name, module_path=module_path, fields=fields, apis=apis)


def load_all_specs(specs_dir: Path) -> dict[str, AdObjectSpec]:
    """Load all spec files from directory."""
    specs = {}

    # First pass: collect all known types
    known_types = set()
    for spec_file in specs_dir.glob("*.json"):
        if spec_file.name != "enum_types.json":
            known_types.add(spec_file.stem)

    # Second pass: load specs with type knowledge
    for spec_file in specs_dir.glob("*.json"):
        if spec_file.name != "enum_types.json":
            try:
                spec = load_spec_file(spec_file, known_types)
                if spec:
                    specs[spec.name] = spec
            except Exception as e:
                print(f"Error loading {spec_file}: {e}")

    return specs


class UnifiedModelGenerator:
    """Generate Pydantic models from AdObject specs."""

    def __init__(self):
        # Load templates
        template_dir = Path(__file__).parent

        # Model template for individual AdObject models (from model_template.jinja2)
        with open(template_dir / "unified_model_template.jinja2") as f:
            self.model_template = Template(f.read())

        # Comprehensive template for all models in one file
        with open(template_dir / "all_models_template.jinja2") as f:
            self.all_models_template = Template(f.read())

    def generate_model_file(
        self, spec: AdObjectSpec, enums: dict[str, EnumInfo], known_types: set[str]
    ) -> str:
        """Generate a single model file for an AdObject."""
        # Collect enums relevant to this model
        model_enums = []
        enum_names_used = set()
        referenced_types = set()
        collected_enum_types = set()

        # Check field types for enums and collect referenced types
        for field in spec.fields:
            if field.field_type in enums:
                if field.field_type not in enum_names_used:
                    model_enums.append(enums[field.field_type])
                    enum_names_used.add(field.field_type)

            # Re-parse the type to collect references and enums
            parse_type_to_python(
                field.field_type,
                known_types,
                is_param=False,
                referenced_types=referenced_types,
                enum_types=collected_enum_types,
            )

        # Check API param types for enums
        for api in spec.apis:
            for param in api.params:
                param_type = param.get("type", "")
                # Parse the type to collect any enum references (handles list[enum], etc.)
                parse_type_to_python(
                    param_type, known_types, is_param=True, enum_types=collected_enum_types
                )

        # Add all collected enum types to model_enums
        for enum_name in collected_enum_types:
            if enum_name in enums and enum_name not in enum_names_used:
                model_enums.append(enums[enum_name])
                enum_names_used.add(enum_name)

        # Prepare field literals
        field_literals = [f'"{field.name}"' for field in spec.fields]

        # Prepare fields dict for template
        fields = {}
        for field in spec.fields:
            fields[field.name] = {
                "name": field.name,
                "python_name": field.python_name,
                "python_type": field.python_type,
            }

        # Prepare param models
        param_models = []
        for api in spec.apis:
            if api.params:
                param_fields = []
                for param in api.params:
                    param_name = param["name"]
                    param_type = param.get("type", "Any")
                    python_name = sanitize_field_name(param_name)

                    # Map type and collect referenced types
                    python_type = parse_type_to_python(
                        param_type, known_types, is_param=True, referenced_types=referenced_types
                    )

                    field_alias = None
                    if python_name != param_name:
                        field_alias = param_name

                    param_fields.append((python_name, python_type, field_alias))

                # Generate method name
                method_name = api.method_name
                model_name = f"{spec.name}{''.join(word.capitalize() for word in method_name.split('_'))}Params"

                param_models.append(
                    {"name": model_name, "method_name": method_name, "fields": param_fields}
                )

        # Generate imports for referenced types
        local_imports = []
        type_checking_imports = []

        # Remove self-reference if present
        referenced_types.discard(spec.name)

        # Sort referenced types for consistent output
        for ref_type in sorted(referenced_types):
            module_name = ref_type.lower()
            # Use relative import
            import_stmt = f"from .{module_name} import {ref_type}Fields"
            # Put all imports under TYPE_CHECKING to avoid circular import issues
            type_checking_imports.append(import_stmt)

        # Render template
        context = {
            "class_name": spec.name,
            "module_path": spec.module_path,
            "enums": model_enums,
            "field_literals": field_literals,
            "fields": fields,
            "param_models": param_models,
            "type_checking_imports": type_checking_imports,
            "local_imports": local_imports,
            "manual_sections": {},  # No manual sections for spec-generated files
        }

        return self.model_template.render(**context)

    def generate_all_models_file(
        self, specs: dict[str, AdObjectSpec], enums: dict[str, EnumInfo]
    ) -> str:
        """Generate a single file with all models."""
        # Render template
        context = {"specs": specs, "enums": enums}

        return self.all_models_template.render(**context)


def main():
    """Main function to generate models from API specs."""
    import subprocess

    # Paths
    specs_dir = Path("api_specs/specs")
    enum_file = specs_dir / "enum_types.json"
    models_dir = Path("src/generated/models")
    models_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading enum types from {enum_file}...")
    enums = load_enum_types(enum_file)
    print(f"Loaded {len(enums)} enum types")

    print(f"\nLoading specs from {specs_dir}...")
    specs = load_all_specs(specs_dir)
    print(f"Loaded {len(specs)} AdObject specs")

    # Initialize generator
    generator = UnifiedModelGenerator()

    # Generate individual model files
    print("\nGenerating individual model files...")
    generated_files = []
    known_types = set(specs.keys())
    for spec_name, spec in sorted(specs.items()):
        output_file = models_dir / f"{spec.module_path}.py"
        content = generator.generate_model_file(spec, enums, known_types)

        with open(output_file, "w") as f:
            f.write(content)

        generated_files.append(output_file)
        print(f"  ✓ Generated {output_file}")
        print(f"    - {len(spec.fields)} fields")
        print(f"    - {len(spec.apis)} API methods")

    # Generate __init__.py
    print("\nGenerating __init__.py...")
    init_file = models_dir / "__init__.py"
    with open(init_file, "w") as f:
        f.write('"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""\n')
        f.write('"""Auto-generated Pydantic models for Facebook Business SDK objects."""\n\n')
        # Include all generated model files
        for spec_name in sorted(specs.keys()):
            module_path = specs[spec_name].module_path
            f.write(f"from .{module_path} import *  # noqa: F403\n")

    print(f"  ✓ Generated {init_file}")

    # Generate comprehensive file
    print("\nGenerating comprehensive models file...")
    all_models_file = models_dir.parent / "models.py"
    content = generator.generate_all_models_file(specs, enums)

    with open(all_models_file, "w") as f:
        f.write(content)

    print(f"  ✓ Generated {all_models_file}")

    # Format with ruff
    print("\nFormatting generated files...")
    try:
        subprocess.run("uv run ruff format src/generated/", shell=True, check=True)
        subprocess.run("uv run ruff check src/generated/ --fix", shell=True, check=True)
        print("  ✓ Formatted with ruff")
    except subprocess.CalledProcessError:
        print("  ⚠ Warning: ruff formatting failed")

    print(f"\n✅ Successfully generated models for {len(specs)} AdObjects")
    print(f"   - {len(generated_files)} individual model files")
    print("   - 1 comprehensive models.py file")
    print(f"   - {len(enums)} enum types")


if __name__ == "__main__":
    main()
