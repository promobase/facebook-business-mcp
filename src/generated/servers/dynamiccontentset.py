"""DynamicContentSet MCP Server."""

from typing import Any

from facebook_business.adobjects.dynamiccontentset import DynamicContentSet
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookDynamicContentSet"
instructions = """
DynamicContentSet MCP Server for Facebook Business API.

Provides typed access to all DynamicContentSet operations.
"""

dynamiccontentset_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@dynamiccontentset_server.tool
@wrapped_fn_tool
def get_dynamiccontentset(
    dynamiccontentset_id: str,
    fields: list[str] = [],
) -> str:
    obj = DynamicContentSet(dynamiccontentset_id)
    return obj.api_get(fields=fields)
