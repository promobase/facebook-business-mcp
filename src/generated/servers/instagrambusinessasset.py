"""InstagramBusinessAsset MCP Server."""

from typing import Any

from facebook_business.adobjects.instagrambusinessasset import InstagramBusinessAsset
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookInstagramBusinessAsset"
instructions = """
InstagramBusinessAsset MCP Server for Facebook Business API.

Provides typed access to all InstagramBusinessAsset operations.
"""

instagrambusinessasset_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@instagrambusinessasset_server.tool
@wrapped_fn_tool
def get_instagrambusinessasset(
    instagrambusinessasset_id: str,
    fields: list[str] = [],
) -> str:
    obj = InstagramBusinessAsset(instagrambusinessasset_id)
    return obj.api_get(fields=fields)
