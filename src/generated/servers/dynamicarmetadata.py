"""DynamicARMetadata MCP Server."""

from typing import Any

from facebook_business.adobjects.dynamicarmetadata import DynamicARMetadata
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookDynamicARMetadata"
instructions = """
DynamicARMetadata MCP Server for Facebook Business API.

Provides typed access to all DynamicARMetadata operations.
"""

dynamicarmetadata_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@dynamicarmetadata_server.tool
@wrapped_fn_tool
def get_dynamicarmetadata(
    dynamicarmetadata_id: str,
    fields: list[str] = [],
) -> str:
    obj = DynamicARMetadata(dynamicarmetadata_id)
    return obj.api_get(fields=fields)
