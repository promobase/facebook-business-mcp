"""InstagramUser MCP Server."""

from typing import Any

from facebook_business.adobjects.instagramuser import InstagramUser
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookInstagramUser"
instructions = """
InstagramUser MCP Server for Facebook Business API.

Provides typed access to all InstagramUser operations.
"""

instagramuser_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@instagramuser_server.tool
@wrapped_fn_tool
def get_instagramuser(
    instagramuser_id: str,
    fields: list[str] = [],
) -> str:
    obj = InstagramUser(instagramuser_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@instagramuser_server.tool
@wrapped_fn_tool
def get_authorized_ad_accounts(
    instagramuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return InstagramUser(instagramuser_id).get_authorized_ad_accounts(fields=fields, params=params)
