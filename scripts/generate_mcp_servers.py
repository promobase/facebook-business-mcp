#!/usr/bin/env python3
"""
Generate MCP servers by parsing methods directly from Facebook Business SDK Python files.

This script uses AST to extract all method definitions from the SDK and generates
MCP server wrappers that call these exact methods, ensuring 100% compatibility.
"""

import ast
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from jinja2 import Template


@dataclass
class MethodInfo:
    """Information about a method extracted from SDK."""

    name: str
    params: list[str]
    is_crud: bool  # api_get, api_update, api_delete, api_create
    is_edge: bool  # get_*, create_*, delete_*, etc.
    http_method: Optional[str] = None  # GET, POST, DELETE
    endpoint: Optional[str] = None
    docstring: Optional[str] = None

    @property
    def is_api_method(self) -> bool:
        """Check if this is an API method (CRUD or edge)."""
        return self.is_crud or self.is_edge

    @property
    def method_type(self) -> str:
        """Get the method type for categorization."""
        if self.is_crud:
            if self.name == "api_get":
                return "read"
            elif self.name == "api_update":
                return "update"
            elif self.name == "api_delete":
                return "delete"
            elif self.name == "api_create":
                return "create"
        elif self.is_edge:
            if self.name.startswith("get_"):
                return "get_edge"
            elif self.name.startswith("create_"):
                return "create_edge"
            elif self.name.startswith("delete_"):
                return "delete_edge"
        return "other"


@dataclass
class AdObjectInfo:
    """Information about a Facebook AdObject extracted from SDK."""

    name: str  # e.g., "Campaign"
    module_path: str  # e.g., "campaign"
    class_name: str  # e.g., "Campaign"
    parent_classes: list[str] = field(default_factory=list)
    methods: dict[str, MethodInfo] = field(default_factory=dict)
    fields: list[str] = field(default_factory=list)

    @property
    def has_crud(self) -> bool:
        """Check if this object has any CRUD methods."""
        return any(m.is_crud for m in self.methods.values())

    @property
    def has_edges(self) -> bool:
        """Check if this object has any edge methods."""
        return any(m.is_edge for m in self.methods.values())

    @property
    def needs_server(self) -> bool:
        """Check if this object needs an MCP server."""
        return self.has_crud or self.has_edges


class SDKMethodParser:
    """Parser for Facebook SDK Python files using AST."""

    def __init__(self, sdk_path: str):
        self.sdk_path = Path(sdk_path)
        self.adobjects_path = self.sdk_path / "facebook_business" / "adobjects"

    def find_adobject_files(self) -> list[Path]:
        """Find all AdObject Python files in the SDK."""
        if not self.adobjects_path.exists():
            return []

        # Skip these files as they're not actual AdObjects
        skip_files = {
            "__init__.py",
            "abstractobject.py",
            "abstractcrudobject.py",
            "objectparser.py",
            "serverside",
        }

        files = []
        for file_path in self.adobjects_path.glob("*.py"):
            if file_path.name not in skip_files and not file_path.name.startswith("_"):
                files.append(file_path)

        return sorted(files)

    def parse_method_node(self, node: ast.FunctionDef) -> MethodInfo:
        """Parse a method AST node to extract method information."""
        # Get method name
        name = node.name

        # Get parameters (skip 'self')
        params = []
        for arg in node.args.args[1:]:  # Skip 'self'
            params.append(arg.arg)

        # Check if it's a CRUD method
        is_crud = name in ["api_get", "api_update", "api_delete", "api_create"]

        # Check if it's an edge method (public method that makes API calls)
        is_edge = False
        if not is_crud and not name.startswith("_"):
            # Check if method contains FacebookRequest
            for child in ast.walk(node):
                if isinstance(child, ast.Call):
                    if isinstance(child.func, ast.Name) and child.func.id == "FacebookRequest":
                        is_edge = True
                        break

        # Extract HTTP method and endpoint from FacebookRequest if possible
        http_method = None
        endpoint = None

        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                if isinstance(child.func, ast.Name) and child.func.id == "FacebookRequest":
                    # Extract method and endpoint from kwargs
                    for keyword in child.keywords:
                        if keyword.arg == "method":
                            if isinstance(keyword.value, ast.Constant):
                                http_method = keyword.value.value
                        elif keyword.arg == "endpoint":
                            if isinstance(keyword.value, ast.Constant):
                                endpoint = keyword.value.value

        # Get docstring
        docstring = ast.get_docstring(node)

        return MethodInfo(
            name=name,
            params=params,
            is_crud=is_crud,
            is_edge=is_edge,
            http_method=http_method,
            endpoint=endpoint,
            docstring=docstring,
        )

    def parse_adobject_file(self, file_path: Path) -> Optional[AdObjectInfo]:
        """Parse a single AdObject file to extract class and method information."""
        try:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Parse AST
            tree = ast.parse(content)

            # Find the main class (usually matches the filename)
            module_name = file_path.stem
            class_name = None
            main_class = None

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    # Look for a class that matches the module name (case-insensitive)
                    if node.name.lower() == module_name.lower():
                        class_name = node.name
                        main_class = node
                        break

            if not main_class:
                # Try to find the first class that inherits from AbstractCrudObject
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        for base in node.bases:
                            if isinstance(base, ast.Name) and base.id == "AbstractCrudObject":
                                class_name = node.name
                                main_class = node
                                break
                        if main_class:
                            break

            if not main_class:
                return None

            # Extract parent classes
            parent_classes = []
            for base in main_class.bases:
                if isinstance(base, ast.Name):
                    parent_classes.append(base.id)

            # Extract methods
            methods = {}

            # Check if class inherits from AbstractCrudObject
            inherits_crud = "AbstractCrudObject" in parent_classes

            # Look for get_endpoint method
            endpoint = None
            for node in main_class.body:
                if isinstance(node, ast.FunctionDef) and node.name == "get_endpoint":
                    # Try to extract the return value
                    for child in ast.walk(node):
                        if isinstance(child, ast.Return) and isinstance(child.value, ast.Constant):
                            endpoint = child.value.value
                            break

            # If it inherits from AbstractCrudObject, assume it has all CRUD methods
            if inherits_crud:
                # Add default CRUD methods
                crud_method_names = ["api_get", "api_create", "api_update", "api_delete"]
                for method_name in crud_method_names:
                    # Default params based on the method
                    if method_name == "api_create":
                        params = [
                            "parent_id",
                            "fields",
                            "params",
                            "batch",
                            "success",
                            "failure",
                            "pending",
                        ]
                    else:
                        params = ["fields", "params", "batch", "success", "failure", "pending"]

                    methods[method_name] = MethodInfo(
                        name=method_name,
                        params=params,
                        is_crud=True,
                        is_edge=False,
                        http_method="POST"
                        if method_name in ["api_create", "api_update"]
                        else ("DELETE" if method_name == "api_delete" else "GET"),
                        endpoint=endpoint,
                        docstring=f"Standard {method_name} method inherited from AbstractCrudObject",
                    )

            # Parse methods in the class body (these might override the inherited ones)
            for node in main_class.body:
                if isinstance(node, ast.FunctionDef):
                    method_info = self.parse_method_node(node)
                    if method_info.is_api_method:
                        # Override any inherited method with the actual implementation
                        methods[method_info.name] = method_info

            # Extract fields from Field class if it exists
            fields = []
            for node in main_class.body:
                if isinstance(node, ast.ClassDef) and node.name == "Field":
                    for field_node in node.body:
                        if isinstance(field_node, ast.Assign):
                            for target in field_node.targets:
                                if isinstance(target, ast.Name):
                                    fields.append(target.id)

            return AdObjectInfo(
                name=class_name,
                module_path=module_name,
                class_name=class_name,
                parent_classes=parent_classes,
                methods=methods,
                fields=fields,
            )

        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return None


class MCPServerGenerator:
    """Generate MCP servers from parsed SDK methods."""

    def __init__(self):
        # Load templates
        template_path = Path(__file__).parent / "server_template_sdk.jinja2"
        with open(template_path) as f:
            self.server_template = Template(f.read())

        init_template_path = Path(__file__).parent / "init_template.jinja2"
        with open(init_template_path) as f:
            self.init_template = Template(f.read())

    def generate_server_file(self, adobject_info: AdObjectInfo, output_dir: Path) -> Path:
        """Generate an MCP server file for an AdObject."""
        # Group methods by type
        crud_methods = []
        edge_methods = []

        for method in adobject_info.methods.values():
            if method.is_crud:
                crud_methods.append(method)
            elif method.is_edge:
                edge_methods.append(method)

        # Sort methods
        crud_methods.sort(key=lambda m: m.name)
        edge_methods.sort(key=lambda m: m.name)

        # Prepare template context
        context = {
            "object_name": adobject_info.name,
            "module_path": adobject_info.module_path,
            "class_name": adobject_info.class_name,
            "crud_methods": crud_methods,
            "edge_methods": edge_methods,
            "has_crud": len(crud_methods) > 0,
            "has_edges": len(edge_methods) > 0,
        }

        # Render template
        content = self.server_template.render(**context)

        # Write file
        output_file = output_dir / f"{adobject_info.module_path}.py"
        with open(output_file, "w") as f:
            f.write(content)

        return output_file

    def generate_init_file(self, adobject_infos: list[AdObjectInfo], output_dir: Path):
        """Generate __init__.py to export all servers."""
        # Filter objects that need servers
        server_objects = [obj for obj in adobject_infos if obj.needs_server]

        # Sort by module path
        server_objects.sort(key=lambda x: x.module_path)

        # Create server info for template
        servers = []
        for obj in server_objects:
            servers.append(
                {
                    "module_path": obj.module_path,
                    "object_name": obj.name,
                    "server_name": f"Facebook{obj.name}",
                    "variable_name": f"{obj.module_path}_server",
                }
            )

        # Render template
        content = self.init_template.render(servers=servers)

        # Write file
        init_file = output_dir / "__init__.py"
        with open(init_file, "w") as f:
            f.write(content)


def main():
    """Generate MCP servers by parsing SDK methods."""
    # Create template if it doesn't exist
    template_path = Path(__file__).parent / "server_template_sdk.jinja2"
    if not template_path.exists():
        raise FileNotFoundError(
            f"Template file not found: {template_path}. Please create it based on the example."
        )

    # Initialize parser
    sdk_path = "/Users/ruizeli/dev/promobase/facebook-python-business-sdk"
    parser = SDKMethodParser(sdk_path)

    # Output directory
    output_dir = Path("facebook_business_mcp/generated/servers")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Find and parse all AdObject files
    print("Scanning Facebook SDK for AdObject files...")
    adobject_files = parser.find_adobject_files()
    print(f"Found {len(adobject_files)} AdObject files")

    # Parse each file
    adobject_infos = []
    total_methods = 0

    for file_path in adobject_files:
        print(f"\nParsing {file_path.name}...")
        adobject_info = parser.parse_adobject_file(file_path)

        if adobject_info and adobject_info.needs_server:
            adobject_infos.append(adobject_info)
            method_count = len(adobject_info.methods)
            total_methods += method_count

            print(f"  ✓ {adobject_info.name}: {method_count} API methods")

            # Show method breakdown
            crud_count = sum(1 for m in adobject_info.methods.values() if m.is_crud)
            edge_count = sum(1 for m in adobject_info.methods.values() if m.is_edge)

            if crud_count > 0:
                crud_names = [m.name for m in adobject_info.methods.values() if m.is_crud]
                print(f"    - CRUD: {crud_count} ({', '.join(crud_names)})")

            if edge_count > 0:
                print(f"    - Edge: {edge_count} methods")
                # Show first few edge method names
                edge_names = [m.name for m in adobject_info.methods.values() if m.is_edge][:5]
                print(f"      Examples: {', '.join(edge_names)}")
                if len(edge_names) < edge_count:
                    print(f"      ... and {edge_count - len(edge_names)} more")

    print(f"\n\nFound {len(adobject_infos)} AdObjects with API methods")
    print(f"Total API methods to wrap: {total_methods}")

    # Generate MCP servers
    generator = MCPServerGenerator()

    print(f"\nGenerating MCP server files in {output_dir}/...")

    for adobject_info in adobject_infos:
        output_file = generator.generate_server_file(adobject_info, output_dir)
        print(f"  ✓ Generated {output_file.name}")

    # Generate __init__.py
    generator.generate_init_file(adobject_infos, output_dir)
    print("\n✓ Generated __init__.py")

    print(f"\n✓ Successfully generated {len(adobject_infos)} MCP servers!")
    print(f"✓ Total methods wrapped: {total_methods}")


if __name__ == "__main__":
    main()
