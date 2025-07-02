"""CatalogItemOverride MCP Server."""

from typing import Any

from facebook_business.adobjects.catalogitemoverride import CatalogItemOverride
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCatalogItemOverride"
instructions = """
CatalogItemOverride MCP Server for Facebook Business API.

Provides typed access to all CatalogItemOverride operations.
"""

catalogitemoverride_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@catalogitemoverride_server.tool
@wrapped_fn_tool
def get_catalogitemoverride(
    catalogitemoverride_id: str,
    fields: list[str] = [],
) -> str:
    obj = CatalogItemOverride(catalogitemoverride_id)
    return obj.api_get(fields=fields)
