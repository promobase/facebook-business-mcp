"""
Generate MCP tool servers for Facebook Business SDK AdObjects.

This script generates streamlined MCP servers for each AdObject that has CRUD operations,
similar to the ad_account.py pattern.
"""

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from generate_models import AdObjectInfo, ApiMethodInfo, FacebookSDKParser


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
    def filename(self) -> str:
        """Get the output filename."""
        return f"{self.module_path}.py"


class MCPToolGenerator:
    """Generate MCP tool servers for AdObjects."""

    def __init__(self):
        self.parser = FacebookSDKParser()

    def analyze_adobject(self, adobject_info: AdObjectInfo) -> Optional[MCPServerInfo]:
        """Analyze an AdObject to determine if it needs an MCP server."""
        if not adobject_info:
            return None

        server_info = MCPServerInfo(
            object_name=adobject_info.name, module_path=adobject_info.module_path
        )

        # Check for CRUD operations
        # First check for methods defined in the AdObject class itself
        for method in adobject_info.instance_methods:
            if method == "api_get":
                server_info.has_api_get = True
            elif method == "api_update":
                server_info.has_api_update = True
                # Check if we have update_params
                if adobject_info.update_params:
                    server_info.has_update_params = True
            elif method == "api_delete":
                server_info.has_api_delete = True

        # Then check for edge methods (API methods)
        for method in adobject_info.api_methods:
            if method.http_method and method.endpoint:
                # Edge methods (get_*, create_*, delete_*)
                server_info.edge_methods.append(method)

        return server_info if server_info.needs_server else None

    def generate_server_file(self, server_info: MCPServerInfo, output_dir: Path) -> Path:
        """Generate an MCP server file for an AdObject."""
        lines = []

        # Header
        lines.append(
            f'"""Streamlined {server_info.object_name} MCP Server - Core Operations Only."""'
        )
        lines.append("")
        lines.append("from __future__ import annotations")
        lines.append("")
        lines.append("from typing import Any")
        lines.append("")
        lines.append(
            f"from facebook_business.adobjects.{server_info.module_path} import {server_info.object_name}"
        )
        lines.append("from fastmcp import FastMCP")
        lines.append("")
        lines.append(
            f"from src.generated.models.{server_info.module_path} import {server_info.object_name}Field"
        )
        if server_info.has_update_params:
            lines.append(
                f"from src.generated.models.{server_info.module_path} import {server_info.object_name}UpdateParams"
            )
        lines.append("from src.utils import wrapped_fn_tool")

        # Don't import wrappers module anymore, we'll import individual functions

        lines.append("")
        lines.append("# Server setup")
        lines.append(f'server_name = "{server_info.server_name}"')
        lines.append('instructions = """')
        lines.append(f"{server_info.object_name} MCP Server for Facebook Business API.")
        lines.append("")
        lines.append(f"Provides typed access to all {server_info.object_name} operations.")
        lines.append('"""')
        lines.append("")
        lines.append(f"{server_info.module_path}_server = FastMCP(")
        lines.append("    name=server_name,")
        lines.append("    instructions=instructions,")
        lines.append(")")
        lines.append("")
        lines.append("")

        # CRUD Operations section
        crud_count = sum(
            [server_info.has_api_get, server_info.has_api_update, server_info.has_api_delete]
        )
        if crud_count > 0:
            lines.append(f"# ---- CRUD Operations ({crud_count}) ----")

            if server_info.has_api_get:
                lines.extend(self._generate_get_method(server_info))

            if server_info.has_api_update:
                lines.extend(self._generate_update_method(server_info))

            if server_info.has_api_delete:
                lines.extend(self._generate_delete_method(server_info))

        # Edge methods section
        edge_count = len(server_info.edge_methods)
        if edge_count > 0:
            lines.append(f"# ---- Edge Methods ({edge_count}) ----")
            lines.append("# Import and register wrapper functions from generated wrappers")

            # Generate imports for all edge methods
            for method in server_info.edge_methods:
                lines.append(
                    f"from src.generated.wrappers.{server_info.module_path}_wrappers import {method.name}"
                )
            lines.append("")

        # Register tools section
        lines.append("")
        lines.append("# ---- Register tools ----")
        lines.append("# Register CRUD operations")
        if server_info.has_api_get:
            lines.append(f"{server_info.module_path}_server.tool(get_{server_info.module_path})")
        if server_info.has_api_update:
            lines.append(f"{server_info.module_path}_server.tool(update_{server_info.module_path})")
        if server_info.has_api_delete:
            lines.append(f"{server_info.module_path}_server.tool(delete_{server_info.module_path})")

        if edge_count > 0:
            lines.append("")
            lines.append("# Register edge methods from wrappers")
            for method in server_info.edge_methods:
                lines.append(f"{server_info.module_path}_server.tool({method.name})")

        lines.append("")

        # Write file
        output_file = output_dir / server_info.filename
        with open(output_file, "w") as f:
            f.write("\n".join(lines))

        return output_file

    def _generate_get_method(self, server_info: MCPServerInfo) -> list[str]:
        """Generate a get method for an object."""
        lines = []
        lines.append("@wrapped_fn_tool")
        lines.append(f"def get_{server_info.module_path}(")
        lines.append(f"    {server_info.module_path}_id: str,")
        lines.append(f"    fields: list[{server_info.object_name}Field] = [],")
        lines.append(") -> str:")
        lines.append(f'    """Get a {server_info.object_name} object by ID.')
        lines.append("    ")
        lines.append("    Args:")
        lines.append(
            f"        {server_info.module_path}_id: The ID of the {server_info.object_name}."
        )
        lines.append("        fields: Fields to retrieve.")
        lines.append('    """')
        lines.append(f"    obj = {server_info.object_name}({server_info.module_path}_id)")
        lines.append("    return obj.api_get(fields=fields)")
        lines.append("")
        lines.append("")
        return lines

    def _generate_update_method(self, server_info: MCPServerInfo) -> list[str]:
        """Generate an update method for an object."""
        lines = []

        # Determine params type
        if server_info.has_update_params:
            params_type = f"{server_info.object_name}UpdateParams | dict[str, Any]"
        else:
            params_type = "dict[str, Any]"

        lines.append("@wrapped_fn_tool")
        lines.append(f"def update_{server_info.module_path}(")
        lines.append(f"    {server_info.module_path}_id: str,")
        lines.append(f"    fields: list[{server_info.object_name}Field] = [],")
        lines.append(f"    params: {params_type} = {{}},")
        lines.append(") -> str:")
        lines.append(f'    """Update a {server_info.object_name} object.')
        lines.append("    ")
        lines.append("    Args:")
        lines.append(
            f"        {server_info.module_path}_id: The ID of the {server_info.object_name}."
        )
        lines.append("        fields: Fields to return after update.")
        lines.append("        params: Parameters to update.")
        lines.append('    """')
        lines.append(
            f"    return {server_info.object_name}({server_info.module_path}_id).api_update(fields=fields, params=params)"
        )
        lines.append("")
        lines.append("")
        return lines

    def _generate_delete_method(self, server_info: MCPServerInfo) -> list[str]:
        """Generate a delete method for an object."""
        lines = []
        lines.append("@wrapped_fn_tool")
        lines.append(f"def delete_{server_info.module_path}(")
        lines.append(f"    {server_info.module_path}_id: str,")
        lines.append(") -> str:")
        lines.append(f'    """Delete a {server_info.object_name} object.')
        lines.append("    ")
        lines.append("    Args:")
        lines.append(
            f"        {server_info.module_path}_id: The ID of the {server_info.object_name}."
        )
        lines.append('    """')
        lines.append(
            f"    return {server_info.object_name}({server_info.module_path}_id).api_delete()"
        )
        lines.append("")
        lines.append("")
        return lines

    def _generate_dynamic_fallback(self, server_info: MCPServerInfo) -> list[str]:
        """Generate dynamic fallback method."""
        lines = []
        lines.append("@wrapped_fn_tool")
        lines.append(f"def run_any_{server_info.module_path}_fn(")
        lines.append(f"    {server_info.module_path}_id: str,")
        lines.append("    fn: str,")
        lines.append("    args: list[str] = [],")
        lines.append("    kwargs: dict[str, Any] = {},")
        lines.append(") -> str:")
        lines.append(f'    """Dynamically call any method on the {server_info.object_name} object.')
        lines.append("    ")
        lines.append("    Use this for operations not covered by the core tools above.")
        lines.append("    ")
        lines.append("    Args:")
        lines.append(
            f"        {server_info.module_path}_id: The ID of the {server_info.object_name}."
        )
        lines.append(f"        fn: Method name to call on {server_info.object_name} object.")
        lines.append("        args: Positional arguments for the method.")
        lines.append("        kwargs: Keyword arguments for the method.")
        lines.append('    """')
        lines.append(f"    obj = {server_info.object_name}({server_info.module_path}_id)")
        lines.append("    if not hasattr(obj, fn):")
        lines.append(
            f"        return f\"{server_info.object_name} does not have method '{{fn}}'.\""
        )
        lines.append("    f = getattr(obj, fn)")
        lines.append("    if not callable(f):")
        lines.append(
            f'        return f"{{fn}} is not a callable method on {server_info.object_name}."'
        )
        lines.append("    return str(f(*args, **kwargs))")
        lines.append("")
        return lines

    def generate_init_file(self, server_infos: list[MCPServerInfo], output_dir: Path):
        """Generate __init__.py to export all servers."""
        lines = []
        lines.append('"""MCP servers for Facebook Business SDK resources."""')
        lines.append("")

        # Import all servers
        for info in sorted(server_infos, key=lambda x: x.module_path):
            lines.append(f"from .{info.module_path} import {info.module_path}_server")

        lines.append("")
        lines.append("__all__ = [")
        for info in sorted(server_infos, key=lambda x: x.module_path):
            lines.append(f'    "{info.module_path}_server",')
        lines.append("]")
        lines.append("")

        init_file = output_dir / "__init__.py"
        with open(init_file, "w") as f:
            f.write("\n".join(lines))


def main():
    """Generate MCP tool servers for all AdObjects with CRUD operations."""
    generator = MCPToolGenerator()
    parser = generator.parser

    # Output directory
    output_dir = Path("src/generated/servers")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process all AdObject files
    adobject_files = parser.find_adobject_files()

    # Filter and analyze
    server_infos = []
    total_crud_objects = 0
    total_edge_methods = 0

    print("Analyzing AdObjects for MCP server generation...")

    for file_path in adobject_files:
        # Skip special files
        if file_path.stem.startswith("__") or file_path.stem in [
            "abstractobject",
            "abstractcrudobject",
            "apispecfile",
        ]:
            continue

        adobject_info = parser.parse_file(file_path)
        if adobject_info:
            server_info = generator.analyze_adobject(adobject_info)
            if server_info:
                server_infos.append(server_info)
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

    # Define important AdObjects that users commonly use
    important_objects = {
        "adaccount": "Core resource for managing ads",
        "campaign": "Top-level advertising campaigns",
        "adset": "Ad sets within campaigns",
        "ad": "Individual ads",
        "adcreative": "Creative assets for ads",
        "customaudience": "Custom audiences for targeting",
        "business": "Business/organization management",
        "page": "Facebook pages",
        "iguser": "Instagram accounts",
        "adimage": "Ad images",
        "advideo": "Ad videos",
        "productcatalog": "Product catalogs for e-commerce",
        "productfeed": "Product feeds",
        "productset": "Product sets",
        "adspixel": "Facebook pixel for tracking",
    }

    # Filter server infos to only include important objects
    important_server_infos = []
    other_server_infos = []

    for server_info in server_infos:
        if server_info.module_path in important_objects:
            important_server_infos.append(server_info)
        else:
            other_server_infos.append(server_info)

    print(f"\nFound {len(important_server_infos)} important AdObjects to generate:")
    for info in important_server_infos:
        desc = important_objects.get(info.module_path, "")
        print(f"  - {info.object_name}: {desc}")

    # Generate server files for important objects
    print(f"\nGenerating MCP server files in {output_dir}/...")

    generated_infos = []
    for server_info in important_server_infos:
        output_file = generator.generate_server_file(server_info, output_dir)
        generated_infos.append(server_info)
        print(f"  ✓ Generated {output_file.name}")
        print(
            f"    - CRUD: get={server_info.has_api_get}, update={server_info.has_api_update}, delete={server_info.has_api_delete}"
        )
        print(f"    - Edge methods: {len(server_info.edge_methods)}")

    # Generate __init__.py
    generator.generate_init_file(generated_infos, output_dir)
    print("\n✓ Generated __init__.py")

    print(f"\n✓ Generated {len(generated_infos)} MCP server files for important AdObjects")
    print(f"  Total objects with servers available: {len(server_infos)}")


if __name__ == "__main__":
    main()
