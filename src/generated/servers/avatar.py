"""Avatar MCP Server."""

from typing import Any

from facebook_business.adobjects.avatar import Avatar
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAvatar"
instructions = """
Avatar MCP Server for Facebook Business API.

Provides typed access to all Avatar operations.
"""

avatar_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@avatar_server.tool
@wrapped_fn_tool
def get_avatar(
    avatar_id: str,
    fields: list[str] = [],
) -> str:
    obj = Avatar(avatar_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@avatar_server.tool
@wrapped_fn_tool
def get_models(
    avatar_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Avatar(avatar_id).get_models(fields=fields, params=params)
