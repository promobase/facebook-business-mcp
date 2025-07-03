#!/usr/bin/env python3
"""
Generate a single unified models file from Facebook API specs.
This avoids forward reference issues by having all models in one file.
"""

import json
import subprocess
from pathlib import Path

from generate_models_unified import (
    UnifiedModelGenerator,
    load_all_specs,
    load_enum_types,
)


def main():
    """Main function to generate a single models file from API specs."""
    # Paths
    specs_dir = Path("api_specs/specs")
    enum_file = specs_dir / "enum_types.json"
    models_dir = Path("facebook_business_mcp/generated/models")
    models_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading enum types from {enum_file}...")
    enums = load_enum_types(enum_file)
    print(f"Loaded {len(enums)} enum types")

    print(f"\nLoading specs from {specs_dir}...")
    specs = load_all_specs(specs_dir)
    print(f"Loaded {len(specs)} AdObject specs")

    # Initialize generator
    generator = UnifiedModelGenerator()

    # Generate single unified file using the all_models template
    print("\nGenerating single unified models file...")
    output_file = models_dir / "generated_models.py"

    # Process specs to add computed fields needed by the template
    from generate_models_unified import parse_type_to_python, sanitize_field_name

    known_types = set(specs.keys())

    for spec in specs.values():
        # Process fields
        for field in spec.fields:
            field.python_name = sanitize_field_name(field.name)
            # Parse the actual type from the field
            python_type = parse_type_to_python(field.field_type, known_types, is_param=False)
            # Add | None for optional fields (all fields are optional in the API)
            field.python_type = f"{python_type} | None"
    # Generate content using the all_models template
    content = generator.generate_all_models_file(specs, enums)

    with open(output_file, "w") as f:
        f.write(content)

    print(f"  ✓ Generated {output_file}")
    print(f"    - {len(specs)} models")
    print(f"    - {sum(len(spec.fields) for spec in specs.values())} total fields")
    print(f"    - {sum(len(spec.apis) for spec in specs.values())} total API methods")

    # Update __init__.py to export from the single file
    init_file = models_dir / "__init__.py"
    with open(init_file, "w") as f:
        f.write('"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""\n\n')
        f.write("# Import everything from the single unified models file\n")
        f.write("from .generated_models import *  # noqa: F403\n")

    print(f"  ✓ Updated {init_file}")

    # Clean up old individual model files
    print("\nCleaning up old model files...")
    for file in models_dir.glob("*.py"):
        if file.name not in ["__init__.py", "generated_models.py", "models.py"]:
            file.unlink()
            print(f"  ✓ Removed {file.name}")

    print("\n✅ Generation complete!")


if __name__ == "__main__":
    main()
