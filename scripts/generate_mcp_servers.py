"""
Generate MCP servers with typed wrappers for Facebook Business SDK AdObjects.

This script generates MCP servers that include both CRUD operations and edge methods
with full type safety using the generated Pydantic models.
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


class MCPServerGenerator:
    """Generate MCP servers with typed wrappers for AdObjects."""

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

    def generate_server_file(
        self, server_info: MCPServerInfo, adobject_info: AdObjectInfo, output_dir: Path
    ) -> Path:
        """Generate an MCP server file for an AdObject."""
        lines = []

        # Header
        lines.append(f'"""{server_info.object_name} MCP Server with typed wrappers."""')
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

        # Import models
        lines.append(
            f"from src.generated.models.{server_info.module_path} import {server_info.object_name}Field"
        )
        if server_info.has_update_params:
            lines.append(
                f"from src.generated.models.{server_info.module_path} import {server_info.object_name}UpdateParams"
            )

        # Import param models for edge methods
        param_model_imports = set()
        for method in server_info.edge_methods:
            param_model_name = f"{server_info.object_name}{''.join(word.capitalize() for word in method.name.split('_'))}Params"
            param_model_imports.add(param_model_name)

        if param_model_imports:
            lines.append(f"from src.generated.models.{server_info.module_path} import (")
            for i, model_name in enumerate(sorted(param_model_imports)):
                comma = "," if i < len(param_model_imports) - 1 else ""
                lines.append(f"    {model_name}{comma}")
            lines.append(")")

        # Import field types for edge methods that return different objects
        field_imports = self._get_field_imports_for_edge_methods(server_info, adobject_info)
        for module, field_type in sorted(field_imports):
            lines.append(f"from src.generated.models.{module} import {field_type}")

        lines.append("from src.utils import wrapped_fn_tool")
        lines.append("")

        # Server setup
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

        # CRUD Operations
        crud_count = sum(
            [server_info.has_api_get, server_info.has_api_update, server_info.has_api_delete]
        )
        if crud_count > 0:
            lines.append(f"# ---- CRUD Operations ({crud_count}) ----")

            if server_info.has_api_get:
                lines.extend(self._generate_get_method(server_info))
                lines.append(
                    f"{server_info.module_path}_server.tool(get_{server_info.module_path})"
                )
                lines.append("")

            if server_info.has_api_update:
                lines.extend(self._generate_update_method(server_info))
                lines.append(
                    f"{server_info.module_path}_server.tool(update_{server_info.module_path})"
                )
                lines.append("")

            if server_info.has_api_delete:
                lines.extend(self._generate_delete_method(server_info))
                lines.append(
                    f"{server_info.module_path}_server.tool(delete_{server_info.module_path})"
                )
                lines.append("")

        # Edge methods
        edge_count = len(server_info.edge_methods)
        if edge_count > 0:
            lines.append("")
            lines.append(f"# ---- Edge Methods ({edge_count}) ----")

            for method in server_info.edge_methods:
                lines.extend(self._generate_edge_method(server_info, method, adobject_info))
                lines.append(f"{server_info.module_path}_server.tool({method.name})")
                lines.append("")

        # Write file
        output_file = output_dir / server_info.filename
        with open(output_file, "w") as f:
            f.write("\n".join(lines))

        return output_file

    def _get_field_imports_for_edge_methods(
        self, server_info: MCPServerInfo, adobject_info: AdObjectInfo
    ) -> set[tuple[str, str]]:
        """Get field imports needed for edge methods that return different types."""
        imports = set()

        for method in server_info.edge_methods:
            # Determine return type based on method name and target_class
            if method.target_class and method.target_class != server_info.object_name:
                # This method returns a different type
                target_module = method.target_class.lower()
                if method.target_class in self.parser._adobject_types:
                    target_module = self.parser._adobject_types[method.target_class]

                # Special handling for known patterns
                if method.name.startswith("get_"):
                    # GET methods return collections
                    field_type = f"{method.target_class}Field"
                    imports.add((target_module, field_type))

        return imports

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
        return lines

    def _generate_edge_method(
        self, server_info: MCPServerInfo, method: ApiMethodInfo, adobject_info: AdObjectInfo
    ) -> list[str]:
        """Generate an edge method wrapper."""
        lines = []

        # Generate param model name
        param_model_name = f"{server_info.object_name}{''.join(word.capitalize() for word in method.name.split('_'))}Params"

        # Determine return field type
        field_type = f"{server_info.object_name}Field"
        if method.target_class and method.target_class != server_info.object_name:
            field_type = f"{method.target_class}Field"

        lines.append("@wrapped_fn_tool")
        lines.append(f"def {method.name}(")
        lines.append(f"    {server_info.module_path}_id: str,")

        # Add fields parameter for GET methods or methods that return data
        if method.http_method == "GET" or method.name.startswith("get_"):
            lines.append(f"    fields: list[{field_type}] = [],")
        elif method.http_method == "POST" and method.name.startswith("create_"):
            # Some create methods also return fields
            lines.append("    fields: list[str] = [],")

        # Add params parameter
        lines.append(f"    params: {param_model_name} = {{}},")
        lines.append(") -> Any:")

        # Generate docstring
        method_title = " ".join(word.capitalize() for word in method.name.split("_"))
        lines.append(f'    """{method_title} for this {server_info.object_name}.')
        lines.append("")
        lines.append("    Args:")
        lines.append(
            f"        {server_info.module_path}_id: The ID of the {server_info.object_name}."
        )

        if method.http_method == "GET" or method.name.startswith("get_"):
            lines.append("        fields: Fields to retrieve.")
        elif method.http_method == "POST" and method.name.startswith("create_"):
            lines.append("        fields: Fields to retrieve.")

        lines.append("        params: Query parameters.")
        lines.append('    """')

        # Generate method call
        if method.http_method == "GET" or method.name.startswith("get_"):
            lines.append(
                f"    return {server_info.object_name}({server_info.module_path}_id).{method.name}(fields=fields, params=params)"
            )
        elif method.http_method == "POST" and method.name.startswith("create_"):
            lines.append(
                f"    return {server_info.object_name}({server_info.module_path}_id).{method.name}(fields=fields, params=params)"
            )
        else:
            # DELETE methods typically don't have fields
            lines.append(
                f"    return {server_info.object_name}({server_info.module_path}_id).{method.name}(params=params)"
            )

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
    """Generate MCP servers for all AdObjects with CRUD operations."""
    generator = MCPServerGenerator()
    parser = generator.parser

    # Output directory
    output_dir = Path("src/generated/servers")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process all AdObject files
    adobject_files = parser.find_adobject_files()

    # Filter and analyze
    server_infos = []
    adobject_infos = {}
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

    print(f"\n✓ Generated {len(generated_infos)} MCP server files for important AdObjects")
    print(f"  Total objects with servers available: {len(server_infos)}")


if __name__ == "__main__":
    main()
