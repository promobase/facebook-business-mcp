"""BusinessCreativeFolder MCP Server."""

from typing import Any

from facebook_business.adobjects.businesscreativefolder import BusinessCreativeFolder
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessCreativeFolder"
instructions = """
BusinessCreativeFolder MCP Server for Facebook Business API.

Provides typed access to all BusinessCreativeFolder operations.
"""

businesscreativefolder_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@businesscreativefolder_server.tool
@wrapped_fn_tool
def get_businesscreativefolder(
    businesscreativefolder_id: str,
    fields: list[str] = [],
) -> str:
    obj = BusinessCreativeFolder(businesscreativefolder_id)
    return obj.api_get(fields=fields)
