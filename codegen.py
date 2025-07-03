"""
Main codegen script for Facebook Business MCP.

It generates pydantic models and MCP tool servers from the Facebook SDK.
"""

import subprocess
import sys
import time
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Optional

import click


class StepStatus(Enum):
    """Status of a generation step."""

    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED = "skipped"


@dataclass
class GenerationStep:
    """A single code generation step."""

    name: str
    script_path: str
    description: str
    required: bool = True
    depends_on: Optional[list[str]] = None
    status: StepStatus = StepStatus.PENDING
    duration: Optional[float] = None
    error_message: Optional[str] = None

    def __post_init__(self):
        if self.depends_on is None:
            self.depends_on = []


class CodegenRunner:
    """Handles running code generation steps with dependency management."""

    def __init__(self, project_root: Path, verbose: bool = False):
        self.project_root = project_root
        self.verbose = verbose
        self.steps: list[GenerationStep] = []
        self.results = {}

    def add_step(self, step: GenerationStep) -> None:
        """Add a generation step."""
        self.steps.append(step)

    def _print_step_header(self, step: GenerationStep) -> None:
        """Print formatted step header."""
        print(f"\n{'=' * 80}")
        print(f"🔄 {step.description}")
        print(f"   Script: {step.script_path}")
        print(f"{'=' * 80}")

    def _print_step_result(self, step: GenerationStep, success: bool) -> None:
        """Print formatted step result."""
        status_icon = "✅" if success else "❌"
        duration_text = f" ({step.duration:.2f}s)" if step.duration else ""
        print(f"\n{status_icon} {step.description}{duration_text}")

        if not success and step.error_message:
            print(f"   Error: {step.error_message}")

    def _check_dependencies(self, step: GenerationStep) -> bool:
        """Check if all dependencies for a step are satisfied."""
        for dep_name in step.depends_on:
            dep_step = next((s for s in self.steps if s.name == dep_name), None)
            if not dep_step:
                step.error_message = f"Dependency '{dep_name}' not found"
                return False
            if dep_step.status != StepStatus.SUCCESS:
                step.error_message = f"Dependency '{dep_name}' failed or not completed"
                return False
        return True

    def _run_single_step(self, step: GenerationStep) -> bool:
        """Run a single generation step."""
        script_path = self.project_root / step.script_path

        # Check if script exists
        if not script_path.exists():
            step.error_message = f"Script not found: {step.script_path}"
            step.status = StepStatus.FAILED
            return False

        # Check dependencies
        if not self._check_dependencies(step):
            step.status = StepStatus.FAILED
            return False

        step.status = StepStatus.RUNNING
        start_time = time.time()

        try:
            # Run the script
            result = subprocess.run(
                [sys.executable, str(script_path)],
                capture_output=True,
                text=True,
                check=True,
                cwd=self.project_root,
            )

            step.duration = time.time() - start_time

            # Handle output
            if self.verbose or result.stdout:
                if result.stdout.strip():
                    print(result.stdout)

            if result.stderr.strip():
                # Some tools use stderr for info, not errors
                if self.verbose:
                    print(result.stderr, file=sys.stderr)

            step.status = StepStatus.SUCCESS
            return True

        except subprocess.CalledProcessError as e:
            step.duration = time.time() - start_time
            step.status = StepStatus.FAILED
            step.error_message = f"Exit code {e.returncode}"

            if self.verbose:
                if e.stdout:
                    print("STDOUT:", e.stdout)
                if e.stderr:
                    print("STDERR:", e.stderr)

            return False

        except Exception as e:
            step.duration = time.time() - start_time
            step.status = StepStatus.FAILED
            step.error_message = str(e)
            return False

    def run_steps(self, fail_fast: bool = True) -> bool:
        """Run all generation steps in dependency order."""
        print("🚀 Facebook Business MCP - Code Generation")
        print("=" * 50)

        total_steps = len(self.steps)
        completed_steps = 0
        failed_steps = 0

        # Sort steps by dependencies (simple topological sort)
        remaining_steps = self.steps.copy()
        execution_order = []

        while remaining_steps:
            # Find steps with satisfied dependencies
            ready_steps = [
                step
                for step in remaining_steps
                if all(dep in [s.name for s in execution_order] for dep in step.depends_on)
            ]

            if not ready_steps:
                # Circular dependency or missing dependency
                for step in remaining_steps:
                    step.status = StepStatus.FAILED
                    step.error_message = "Circular or missing dependency"
                break

            # Execute ready steps
            for step in ready_steps:
                self._print_step_header(step)
                success = self._run_single_step(step)
                self._print_step_result(step, success)

                execution_order.append(step)
                remaining_steps.remove(step)
                completed_steps += 1

                if not success:
                    failed_steps += 1
                    if fail_fast and step.required:
                        print("\n💥 Required step failed, stopping execution")
                        # Mark remaining steps as skipped
                        for remaining_step in remaining_steps:
                            remaining_step.status = StepStatus.SKIPPED
                        return False

        success = failed_steps == 0
        self._print_summary(total_steps, completed_steps, failed_steps)
        return success

    def _print_summary(self, total: int, completed: int, failed: int) -> None:
        """Print execution summary."""
        print(f"\n{'=' * 80}")
        print("📊 EXECUTION SUMMARY")
        print(f"{'=' * 80}")

        for step in self.steps:
            status_map = {
                StepStatus.SUCCESS: "✅",
                StepStatus.FAILED: "❌",
                StepStatus.SKIPPED: "⏭️",
                StepStatus.PENDING: "⏸️",
            }

            icon = status_map.get(step.status, "❓")
            duration = f" ({step.duration:.2f}s)" if step.duration else ""
            print(f"{icon} {step.name}{duration}")

            if step.error_message:
                print(f"   └─ {step.error_message}")

        print(f"\n📈 Results: {completed - failed}/{total} successful")

        if failed == 0:
            print("\n🎉 All steps completed successfully!")
            self._print_generated_files()
        else:
            print(f"\n⚠️  {failed} step(s) failed")

    def _print_generated_files(self) -> None:
        """Print information about generated files."""
        print("\n📁 Generated files:")

        generated_dirs = [
            ("facebook_business_mcp/generated/models/", "Pydantic models for AdObjects"),
            ("facebook_business_mcp/generated/servers/", "MCP tool servers for AdObjects"),
        ]

        for dir_path, description in generated_dirs:
            full_path = self.project_root / dir_path
            if full_path.exists():
                file_count = len(list(full_path.glob("*.py")))
                print(f"   📄 {dir_path} - {description} ({file_count} files)")

    def run_formatting(self) -> bool:
        """Run code formatting on generated files."""
        print(f"\n{'=' * 80}")
        print("🎨 Running code formatting...")
        print(f"{'=' * 80}")

        commands = [
            ("uv run ruff check . --fix", "Ruff linting with auto-fix"),
            ("uv run ruff format .", "Ruff formatting"),
        ]

        for cmd, description in commands:
            print(f"\n🔧 {description}")
            try:
                result = subprocess.run(
                    cmd,
                    shell=True,
                    check=True,
                    cwd=self.project_root,
                    capture_output=not self.verbose,
                )
                print(f"✅ {description} completed")
            except subprocess.CalledProcessError as e:
                print(f"❌ {description} failed (exit code {e.returncode})")
                return False

        return True


def create_generation_steps() -> list[GenerationStep]:
    """Create the list of generation steps."""
    return [
        GenerationStep(
            name="models",
            script_path="scripts/generate_single_models_file.py",
            description="Generate Pydantic models from Facebook API specs",
            required=True,
        ),
        # GenerationStep(
        #     name="servers",
        #     script_path="scripts/generate_mcp_servers.py",
        #     description="Generate MCP tool servers",
        #     required=True,
        #     depends_on=["models"],  # Servers might depend on models
        # ),
    ]


@click.command()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.option("--no-format", is_flag=True, help="Skip code formatting step")
@click.option(
    "--continue-on-error", is_flag=True, help="Continue execution even if non-critical steps fail"
)
@click.option(
    "--steps", help="Comma-separated list of specific steps to run (e.g., 'models,servers')"
)
def main(verbose: bool, no_format: bool, continue_on_error: bool, steps: Optional[str]):
    """
    Run Facebook Business MCP code generation.

    This script generates Pydantic models and MCP tool servers from the Facebook SDK.
    """
    project_root = Path(__file__).parent

    # Create runner
    runner = CodegenRunner(project_root, verbose=verbose)

    # Add steps
    all_steps = create_generation_steps()

    # Filter steps if specific ones requested
    if steps:
        requested_steps = [s.strip() for s in steps.split(",")]
        all_steps = [step for step in all_steps if step.name in requested_steps]
        if not all_steps:
            click.echo(f"❌ No valid steps found in: {steps}")
            click.echo(f"Available steps: {', '.join(s.name for s in create_generation_steps())}")
            sys.exit(1)

    for step in all_steps:
        runner.add_step(step)

    # Run generation steps
    success = runner.run_steps(fail_fast=not continue_on_error)

    # Run formatting if requested and generation succeeded
    if success and not no_format:
        formatting_success = runner.run_formatting()
        success = success and formatting_success

    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
