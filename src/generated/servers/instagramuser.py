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


# ---- Edge Methods (4) ----
@instagramuser_server.tool
@wrapped_fn_tool
def get_agencies(
    instagramuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return InstagramUser(instagramuser_id).get_agencies(fields=fields, params=params)


@instagramuser_server.tool
@wrapped_fn_tool
def get_ar_effects(
    instagramuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return InstagramUser(instagramuser_id).get_ar_effects(fields=fields, params=params)


@instagramuser_server.tool
@wrapped_fn_tool
def get_authorized_adaccounts(
    instagramuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return InstagramUser(instagramuser_id).get_authorized_adaccounts(fields=fields, params=params)


@instagramuser_server.tool
@wrapped_fn_tool
def get_upcoming_events(
    instagramuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return InstagramUser(instagramuser_id).get_upcoming_events(fields=fields, params=params)
