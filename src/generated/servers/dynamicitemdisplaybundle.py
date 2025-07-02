"""DynamicItemDisplayBundle MCP Server."""

from typing import Any

from facebook_business.adobjects.dynamicitemdisplaybundle import DynamicItemDisplayBundle
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookDynamicItemDisplayBundle"
instructions = """
DynamicItemDisplayBundle MCP Server for Facebook Business API.

Provides typed access to all DynamicItemDisplayBundle operations.
"""

dynamicitemdisplaybundle_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@dynamicitemdisplaybundle_server.tool
@wrapped_fn_tool
def get_dynamicitemdisplaybundle(
    dynamicitemdisplaybundle_id: str,
    fields: list[str] = [],
) -> str:
    obj = DynamicItemDisplayBundle(dynamicitemdisplaybundle_id)
    return obj.api_get(fields=fields)
