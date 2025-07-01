"""
Main code generation script for Facebook Business MCP.

This script runs all code generation steps in the correct order:
1. Generate Pydantic models from Facebook SDK AdObjects
2. Generate type-safe wrapper functions for API methods
"""

import subprocess
import sys
from pathlib import Path


def run_script(script_path: str, description: str) -> bool:
    """Run a script and handle output."""
    print(f"\n{'=' * 60}")
    print(f"Running: {description}")
    print(f"{'=' * 60}\n")

    try:
        result = subprocess.run(
            [sys.executable, script_path], capture_output=True, text=True, check=True
        )

        # Print stdout if any
        if result.stdout:
            print(result.stdout)

        # Print stderr if any (some scripts use stderr for info)
        if result.stderr:
            print(result.stderr, file=sys.stderr)

        print(f"\n✓ {description} completed successfully")
        return True

    except subprocess.CalledProcessError as e:
        print(f"\n✗ {description} failed")
        print(f"Exit code: {e.returncode}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False
    except Exception as e:
        print(f"\n✗ {description} failed with unexpected error: {e}")
        return False


def main():
    """Run all code generation scripts."""
    print("Facebook Business MCP - Code Generation")
    print("======================================")

    # Ensure we're in the right directory
    project_root = Path(__file__).parent

    # List of scripts to run in order
    scripts = [
        ("scripts/generate_models.py", "Generate Pydantic models from Facebook SDK"),
        ("scripts/generate_wrappers.py", "Generate type-safe wrapper functions"),
    ]

    all_success = True

    for script_path, description in scripts:
        full_path = project_root / script_path
        if not full_path.exists():
            print(f"\n✗ Script not found: {script_path}")
            all_success = False
            continue

        if not run_script(str(full_path), description):
            all_success = False
            # Continue running other scripts even if one fails

    # Run ruff formatting on generated code if all generation steps succeeded
    if all_success:
        print(f"\n{'=' * 60}")
        print("Running code formatting...")
        print(f"{'=' * 60}\n")

        # Directories to format
        generated_dirs = [
            project_root / "src/generated/models",
            project_root / "src/generated/wrappers",
        ]

        # Run ruff format
        print("Running ruff format...")
        for directory in generated_dirs:
            if directory.exists():
                try:
                    result = subprocess.run(
                        ["uv", "run", "ruff", "format", str(directory)],
                        capture_output=True,
                        text=True,
                        check=True,
                    )
                    print(f"✓ Formatted {directory.relative_to(project_root)}")
                except subprocess.CalledProcessError as e:
                    print(f"✗ Failed to format {directory.relative_to(project_root)}: {e.stderr}")
                    all_success = False

        print("\nRunning ruff check...")
        cmd = "uv run ruff check . --fix && uv run ruff format ."
        subprocess.run(cmd, check=True, shell=True)

    print(f"\n{'=' * 60}")
    if all_success:
        print("✓ All code generation and formatting completed successfully!")
        print("\nGenerated files:")
        print("  - src/generated/models/*.py - Pydantic models for all AdObjects")
        print("  - src/generated/wrappers/*.py - Type-safe wrapper functions")
    else:
        print("✗ Some code generation steps failed. Please check the errors above.")
        sys.exit(1)
    print(f"{'=' * 60}\n")


if __name__ == "__main__":
    main()
