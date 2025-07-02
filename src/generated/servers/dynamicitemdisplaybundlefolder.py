"""DynamicItemDisplayBundleFolder MCP Server."""

from typing import Any

from facebook_business.adobjects.dynamicitemdisplaybundlefolder import (
    DynamicItemDisplayBundleFolder,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookDynamicItemDisplayBundleFolder"
instructions = """
DynamicItemDisplayBundleFolder MCP Server for Facebook Business API.

Provides typed access to all DynamicItemDisplayBundleFolder operations.
"""

dynamicitemdisplaybundlefolder_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@dynamicitemdisplaybundlefolder_server.tool
@wrapped_fn_tool
def get_dynamicitemdisplaybundlefolder(
    dynamicitemdisplaybundlefolder_id: str,
    fields: list[str] = [],
) -> str:
    obj = DynamicItemDisplayBundleFolder(dynamicitemdisplaybundlefolder_id)
    return obj.api_get(fields=fields)
