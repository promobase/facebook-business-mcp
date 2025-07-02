"""DynamicVideoMetadata MCP Server."""

from typing import Any

from facebook_business.adobjects.dynamicvideometadata import DynamicVideoMetadata
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookDynamicVideoMetadata"
instructions = """
DynamicVideoMetadata MCP Server for Facebook Business API.

Provides typed access to all DynamicVideoMetadata operations.
"""

dynamicvideometadata_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@dynamicvideometadata_server.tool
@wrapped_fn_tool
def get_dynamicvideometadata(
    dynamicvideometadata_id: str,
    fields: list[str] = [],
) -> str:
    obj = DynamicVideoMetadata(dynamicvideometadata_id)
    return obj.api_get(fields=fields)
