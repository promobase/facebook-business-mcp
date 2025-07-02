"""
Generate MCP servers with typed wrappers for Facebook Business SDK AdObjects.

This script generates MCP servers that include both CRUD operations and edge methods
with full type safety using the generated Pydantic models.
"""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from generate_models_unified import AdObjectSpec, ApiMethodInfo, load_spec_file
from jinja2 import Template


@dataclass
class AdObjectInfo:
    """Information about a Facebook AdObject extracted from API specs."""

    name: str  # e.g., "Campaign"
    module_path: str  # e.g., "campaign"
    has_api_get: bool = False
    has_api_update: bool = False
    has_api_delete: bool = False
    api_methods: list[ApiMethodInfo] = field(default_factory=list)  # Edge methods


class APISpecParser:
    """Parser for API spec JSON files to extract AdObject information."""

    def __init__(self):
        # Path to the API specs
        self.specs_path = Path("api_specs/specs")
        # Path to SDK to check which AdObjects have CRUD methods
        self.sdk_path = Path("/Users/ruizeli/dev/promobase/facebook-python-business-sdk")
        self.adobjects_path = self.sdk_path / "facebook_business" / "adobjects"

    def find_spec_files(self) -> list[Path]:
        """Find all spec JSON files."""
        if not self.specs_path.exists():
            return []
        return [f for f in self.specs_path.glob("*.json") if f.name != "enum_types.json"]

    def check_crud_methods(self, module_path: str) -> tuple[bool, bool, bool]:
        """Check if the AdObject has CRUD methods in the SDK."""
        sdk_file = self.adobjects_path / f"{module_path}.py"
        if not sdk_file.exists():
            return False, False, False

        try:
            with open(sdk_file) as f:
                content = f.read()

            has_get = bool(re.search(r"def\s+api_get\s*\(", content))
            has_update = bool(re.search(r"def\s+api_update\s*\(", content))
            has_delete = bool(re.search(r"def\s+api_delete\s*\(", content))

            return has_get, has_update, has_delete
        except:
            return False, False, False

    def parse_spec_file(self, file_path: Path) -> Optional[AdObjectInfo]:
        """Parse a single spec file to extract AdObject information."""
        try:
            # Load spec using the unified loader
            spec = load_spec_file(file_path, set())
            if not spec:
                return None

            # Check for CRUD methods in SDK
            has_get, has_update, has_delete = self.check_crud_methods(spec.module_path)

            # Create AdObjectInfo
            info = AdObjectInfo(
                name=spec.name,
                module_path=spec.module_path,
                has_api_get=has_get,
                has_api_update=has_update,
                has_api_delete=has_delete,
                api_methods=spec.apis,
            )

            return info

        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return None


@dataclass
class MCPServerInfo:
    """Information about an MCP server to generate."""

    object_name: str  # e.g., "Campaign"
    module_path: str  # e.g., "campaign"
    has_api_get: bool = False
    has_api_update: bool = False
    has_api_delete: bool = False
    has_update_params: bool = False  # Whether UpdateParams model exists
    edge_methods: list[ApiMethodInfo] = None

    def __post_init__(self):
        if self.edge_methods is None:
            self.edge_methods = []

    @property
    def needs_server(self) -> bool:
        """Determine if this object needs an MCP server."""
        # Need at least one CRUD operation or edge method
        return (
            self.has_api_get
            or self.has_api_update
            or self.has_api_delete
            or len(self.edge_methods) > 0
        )

    @property
    def server_name(self) -> str:
        """Get the server name."""
        return f"Facebook{self.object_name}"

    @property
    def variable_name(self) -> str:
        """Get the server variable name."""
        return f"{self.module_path}_server"

    @property
    def filename(self) -> str:
        """Get the output filename."""
        return f"{self.module_path}.py"


class MCPServerGenerator:
    """Generate MCP servers with typed wrappers for AdObjects."""

    def __init__(self):
        self.parser = APISpecParser()
        # Load the Jinja templates
        template_path = Path(__file__).parent / "server_template.jinja2"
        with open(template_path) as f:
            self.server_template = Template(f.read())

        init_template_path = Path(__file__).parent / "init_template.jinja2"
        with open(init_template_path) as f:
            self.init_template = Template(f.read())

    def analyze_adobject(self, adobject_info: AdObjectInfo) -> Optional[MCPServerInfo]:
        """Analyze an AdObject to determine if it needs an MCP server."""
        if not adobject_info:
            return None

        server_info = MCPServerInfo(
            object_name=adobject_info.name,
            module_path=adobject_info.module_path,
            has_api_get=adobject_info.has_api_get,
            has_api_update=adobject_info.has_api_update,
            has_api_delete=adobject_info.has_api_delete,
            edge_methods=adobject_info.api_methods,
        )

        return server_info if server_info.needs_server else None

    def generate_server_file(
        self, server_info: MCPServerInfo, adobject_info: AdObjectInfo, output_dir: Path
    ) -> Path:
        """Generate an MCP server file for an AdObject."""
        # Prepare template context
        context = {
            "object_name": server_info.object_name,
            "module_path": server_info.module_path,
            "has_api_get": server_info.has_api_get,
            "has_api_update": server_info.has_api_update,
            "has_api_delete": server_info.has_api_delete,
            "crud_operations": any(
                [server_info.has_api_get, server_info.has_api_update, server_info.has_api_delete]
            ),
            "crud_count": sum(
                [server_info.has_api_get, server_info.has_api_update, server_info.has_api_delete]
            ),
            "edge_methods": server_info.edge_methods,
        }

        # Render the template
        content = self.server_template.render(**context)

        # Write file
        output_file = output_dir / server_info.filename
        with open(output_file, "w") as f:
            f.write(content)

        return output_file

    def generate_init_file(self, server_infos: list[MCPServerInfo], output_dir: Path):
        """Generate __init__.py to export all servers."""
        # Sort servers by module path
        sorted_servers = sorted(server_infos, key=lambda x: x.module_path)

        # Render the template
        content = self.init_template.render(servers=sorted_servers)

        init_file = output_dir / "__init__.py"
        with open(init_file, "w") as f:
            f.write(content)


def main():
    """Generate MCP servers for all AdObjects with CRUD operations."""
    generator = MCPServerGenerator()
    parser = generator.parser

    # Output directory
    output_dir = Path("src/generated/servers")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process all spec files
    spec_files = parser.find_spec_files()

    # Filter and analyze
    server_infos = []
    adobject_infos = {}
    total_crud_objects = 0
    total_edge_methods = 0

    print("Analyzing API specs for MCP server generation...")

    for spec_file in spec_files:
        adobject_info = parser.parse_spec_file(spec_file)
        if adobject_info:
            server_info = generator.analyze_adobject(adobject_info)
            if server_info:
                server_infos.append(server_info)
                adobject_infos[server_info.module_path] = adobject_info
                if (
                    server_info.has_api_get
                    or server_info.has_api_update
                    or server_info.has_api_delete
                ):
                    total_crud_objects += 1
                total_edge_methods += len(server_info.edge_methods)

    print(f"\nFound {len(server_infos)} AdObjects that need MCP servers:")
    print(f"  - {total_crud_objects} with CRUD operations")
    print(f"  - {total_edge_methods} total edge methods")

    # Generate server files for all objects
    print(f"\nGenerating MCP server files in {output_dir}/...")

    generated_infos = []
    for server_info in server_infos:
        adobject_info = adobject_infos[server_info.module_path]
        output_file = generator.generate_server_file(server_info, adobject_info, output_dir)
        generated_infos.append(server_info)
        print(f"  ✓ Generated {output_file.name}")
        print(
            f"    - CRUD: get={server_info.has_api_get}, update={server_info.has_api_update}, delete={server_info.has_api_delete}"
        )
        print(f"    - Edge methods: {len(server_info.edge_methods)}")

    # Generate __init__.py
    generator.generate_init_file(generated_infos, output_dir)
    print("\n✓ Generated __init__.py")

    print(
        f"\n✓ Generated {len(generated_infos)} MCP server files for all AdObjects with CRUD/edge methods"
    )


if __name__ == "__main__":
    main()
