#!/usr/bin/env python3
"""
Unified Pydantic Models Generator
Generates all models and enums in a single file to handle imports properly
"""

import json
import os
import re
from pathlib import Path
from typing import Any

from jinja2 import Template


def load_enum_types(enum_file: str) -> dict[str, list[str]]:
    """Load enum definitions from enum_types.json"""
    try:
        with open(enum_file) as f:
            enum_data = json.load(f)

        enums = {}
        for enum_def in enum_data:
            enum_name = enum_def["name"]
            enum_values = enum_def["values"]
            enums[enum_name] = enum_values

        return enums
    except FileNotFoundError:
        print(f"Warning: {enum_file} not found. No enums will be generated.")
        return {}


def load_specs_from_directory(specs_dir: str) -> dict[str, dict[str, Any]]:
    """Load all JSON specs from specs directory"""
    specs = {}
    specs_path = Path(specs_dir)

    if not specs_path.exists():
        print(f"Warning: {specs_dir} directory not found.")
        return {}

    print(f"Scanning directory: {specs_path}")
    json_files = list(specs_path.glob("*.json"))
    print(f"Found JSON files: {[f.name for f in json_files]}")

    for json_file in json_files:
        try:
            with open(json_file) as f:
                spec_data = json.load(f)
                spec_name = json_file.stem

                # Debug: Print the structure of the loaded data
                print(f"Loaded {spec_name}: type={type(spec_data)}")
                if isinstance(spec_data, dict):
                    print(f"  Keys: {list(spec_data.keys())}")
                elif isinstance(spec_data, list):
                    print(f"   length: {len(spec_data)}")
                    if spec_data and isinstance(spec_data[0], dict):
                        print(f"  First item keys: {list(spec_data[0].keys())}")

                specs[spec_name] = spec_data
        except Exception as e:
            print(f"Error loading {json_file}: {e}")

    return specs


def parse_type_to_python(
    type_str: str,
    enums: dict[str, list[str]],
    known_models: set[str],
    spec_to_model_map: dict[str, str] = None,
) -> str:
    """Convert API type to Python/Pydantic type hint"""

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
            parsed_key = parse_type_to_python(key_type, enums, known_models, spec_to_model_map)
            parsed_value = parse_type_to_python(value_type, enums, known_models, spec_to_model_map)
            return f"dict[{parsed_key}, {parsed_value}]"
        else:
            # Single type map, assume string keys
            parsed_value = parse_type_to_python(inner_types, enums, known_models, spec_to_model_map)
            return f"dict[str, {parsed_value}]"

    # Handle list types
    if type_str.startswith("list<") and type_str.endswith(">"):
        inner_type = type_str[5:-1]  # Remove 'list<' and '>'
        parsed_inner = parse_type_to_python(inner_type, enums, known_models, spec_to_model_map)
        return f"list[{parsed_inner}]"

    # Check if it's an enum type
    if type_str in enums:
        return type_str

    # Check if it's a spec name (like AdAssetFeedAdditionalData)
    if spec_to_model_map and type_str in spec_to_model_map:
        return f'"{spec_to_model_map[type_str]}"'

    # Check if it's a known model/class
    if type_str in known_models:
        return f'"{type_str}"'  # Use forward reference for models

    # If not found in known models, it might be an external type
    # Just use it as-is with forward reference
    # This handles types that might not have spec files

    # Handle enum parameter types
    if "_enum_param" in type_str or type_str.endswith("_enum"):
        for enum_name in enums:
            if enum_name.lower().replace("_", "") in type_str.lower().replace("_", ""):
                return enum_name
        return "str"

    # Basic type lookup
    if type_str in type_mapping:
        return type_mapping[type_str]

    # If not found, assume it's an external model and use forward reference
    return f'"{type_str}"'


def sanitize_enum_member_name(value: str) -> str:
    """Sanitize enum member names to be valid Python identifiers"""
    import re

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


def sanitize_field_name(field_name: str) -> str:
    """Sanitize field names to be valid Python identifiers"""

    # Python reserved keywords that need to be renamed
    reserved_keywords = {
        "from",
        "import",
        "class",
        "def",
        "return",
        "if",
        "else",
        "elif",
        "while",
        "for",
        "break",
        "continue",
        "pass",
        "try",
        "except",
        "finally",
        "with",
        "as",
        "yield",
        "lambda",
        "del",
        "global",
        "nonlocal",
        "assert",
        "True",
        "False",
        "None",
        "and",
        "or",
        "not",
        "in",
        "is",
        "async",
        "await",
    }

    # Pydantic BaseModel reserved attributes that need to be renamed
    pydantic_reserved = {
        "schema",  # conflicts with BaseModel.schema()
        "model_config",
        "model_fields",
        "model_computed_fields",
        "model_extra",
        "model_fields_set",
    }

    # Replace dots and other invalid characters with underscores
    sanitized = re.sub(r"[^a-zA-Z0-9_]", "_", field_name)

    # If field name starts with a digit, prefix it with 'field_'
    if sanitized and sanitized[0].isdigit():
        sanitized = f"field_{sanitized}"

    # If field name is a reserved keyword, append underscore
    if sanitized in reserved_keywords:
        sanitized = f"{sanitized}_"

    # If field name conflicts with Pydantic reserved names, append underscore
    if sanitized in pydantic_reserved:
        sanitized = f"{sanitized}_"

    # If the name becomes empty or just underscores, use a default
    if not sanitized or sanitized.replace("_", "") == "":
        sanitized = "field_unnamed"

    return sanitized


def generate_unified_models(
    specs: dict[str, dict[str, Any]], enums: dict[str, list[str]], output_file: str = "models.py"
):
    """Generate all models and enums in a single file"""

    # Create a mapping from original spec names to generated model names
    spec_to_model_map = {}
    model_names = set()
    for spec_name in specs.keys():
        # Keep the original casing from the filename (without .json extension)
        # The spec_name is already the filename without extension
        model_name = spec_name
        model_names.add(model_name)
        # Store mapping for type resolution
        spec_to_model_map[spec_name] = model_name

    # Process enums to include sanitized member names
    processed_enums = {}
    for enum_name, values in enums.items():
        processed_values = []
        for value in values:
            sanitized_name = sanitize_enum_member_name(value)
            processed_values.append({"name": sanitized_name, "value": value})
        processed_enums[enum_name] = processed_values

    # Template for the unified file
    unified_template = '''"""
This file is code-generated from API specs, Opensource by PromoBase.
DO NOT EDIT MANUALLY.
"""

from enum import Enum
from pydantic import BaseModel, Field, ConfigDict, field_serializer
from typing import Any, Optional, Union
from datetime import datetime


{% if enums %}
# Enums
{% for enum_name, values in enums.items() %}
class {{ enum_name }}(str, Enum):
    """{{ enum_name }} enum values"""
    {% for item in values %}
    {{ item.name }} = "{{ item.value }}"
    {% endfor %}


{% endfor %}
{% endif %}

# Models
{% for model_name, model_data in models.items() %}
class {{ model_name }}(BaseModel):
    """{{ model_name }} model"""
    model_config = ConfigDict(
        extra="allow",
        use_enum_values=True,
        populate_by_name=True
    )
    
    {% for field in model_data.fields %}
    {% if field.sanitized_name != field.name %}
    {{ field.sanitized_name }}: Optional[{{ field.python_type }}] = Field(None, alias="{{ field.name }}", description="{{ field.description }}")
    {% else %}
    {{ field.name }}: Optional[{{ field.python_type }}] = Field(None, description="{{ field.description }}")
    {% endif %}
    {% endfor %}
    
    @field_serializer('*', mode='wrap')
    def serialize_datetime(self, value, handler):
        """Custom serializer for datetime fields"""
        if isinstance(value, datetime):
            return value.isoformat() if value else None
        return handler(value)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "{{ model_name }}":
        """Create instance from dictionary"""
        return cls(**data)
    
    def to_dict(self, exclude_none: bool = True) -> dict[str, Any]:
        """Convert to dictionary"""
        return self.model_dump(exclude_none=exclude_none)


{% endfor %}

# Update forward references
{% for model_name in models.keys() %}
{{ model_name }}.model_rebuild()
{% endfor %}


__all__ = [
    {% for enum_name in enums.keys() %}
    "{{ enum_name }}",
    {% endfor %}
    {% for model_name in models.keys() %}
    "{{ model_name }}",
    {% endfor %}
]
'''

    # Process all models
    models_data = {}
    for spec_name, spec_data in specs.items():
        # Use the original spec name as the model name (preserves CamelCase)
        model_name = spec_name

        processed_fields = []

        # Handle different spec data formats
        fields_data = []
        if isinstance(spec_data, dict):
            if "fields" in spec_data:
                fields_data = spec_data["fields"]
            elif "properties" in spec_data:
                # Handle OpenAPI-style specs
                fields_data = [
                    {"name": k, "type": v.get("type", "Any")}
                    for k, v in spec_data["properties"].items()
                ]
        elif isinstance(spec_data, list):
            # If it's a list, check if it contains field definitions
            if spec_data and isinstance(spec_data[0], dict):
                if "name" in spec_data[0] and "type" in spec_data[0]:
                    fields_data = spec_data
                else:
                    print(f"Warning: Unrecognized list format for {spec_name}")
                    continue
        else:
            print(f"Warning: Unrecognized spec format for {spec_name}: {type(spec_data)}")
            continue

        for field in fields_data:
            if isinstance(field, dict) and "name" in field:
                field_type = parse_type_to_python(
                    field.get("type", "Any"), enums, model_names, spec_to_model_map
                )
                field_name = field["name"]
                sanitized_name = sanitize_field_name(field_name)

                processed_field = {
                    "name": field_name,
                    "sanitized_name": sanitized_name,
                    "python_type": field_type,
                    "description": field.get("description", field_name.replace("_", " ").title()),
                    "required": field.get("required", False),
                }
                processed_fields.append(processed_field)

        # Always add the model, even if it has no fields
        # This ensures types referenced by other models exist
        models_data[model_name] = {"fields": processed_fields}
        if not processed_fields:
            print(f"Warning: No fields found for {spec_name}, creating empty model")

    # Generate the code
    template = Template(unified_template)
    code = template.render(enums=processed_enums, models=models_data)

    # Write to file
    with open(output_file, "w") as f:
        f.write(code)

    print(f"✅ Generated unified models file: {output_file}")
    print(f"Generated {len(models_data)} models and {len(enums)} enums")
    print(f"Models: {', '.join(models_data.keys())}")

    return output_file


def find_enum_file() -> str:
    """Find enum_types.json in common locations"""
    possible_paths = [
        "api_specs/specs/enum_types.json",
    ]

    for path in possible_paths:
        if os.path.exists(path):
            print(f"Found enum file at: {path}")
            return path

    print("No enum_types.json file found in common locations")
    return None


def fmt():
    import subprocess

    subprocess.run("uv run ruff format . && uv run ruff check . --fix", shell=True, check=True)


def main():
    """Main function"""
    import sys

    # Configuration
    specs_dir = "api_specs/specs"
    enum_file = None
    output_file = "src/generated/models.py"

    # Override with command line args
    if len(sys.argv) > 1:
        specs_dir = sys.argv[1]
    if len(sys.argv) > 2:
        enum_file = sys.argv[2]
    if len(sys.argv) > 3:
        output_file = sys.argv[3]

    # Auto-find enum file if not specified
    if not enum_file:
        enum_file = find_enum_file()

    print(f"Loading specs from: {specs_dir}")
    print(f"Loading enums from: {enum_file or 'None'}")
    print(f"Output file: {output_file}")

    # Load data
    enums = load_enum_types(enum_file) if enum_file else {}
    specs = load_specs_from_directory(specs_dir)

    if not specs:
        print("No specs found. Checking subdirectories...")
        # Try specs subdirectory
        sub_specs_dir = os.path.join(specs_dir, "specs")
        if os.path.exists(sub_specs_dir):
            print(f"Trying subdirectory: {sub_specs_dir}")
            specs = load_specs_from_directory(sub_specs_dir)

    if not specs:
        print("No specs found. Exiting.")
        return

    # Generate unified models
    generate_unified_models(specs, enums, output_file)
    fmt()


if __name__ == "__main__":
    main()
