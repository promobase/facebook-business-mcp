"""Profile MCP Server."""

from typing import Any

from facebook_business.adobjects.profile import Profile
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProfile"
instructions = """
Profile MCP Server for Facebook Business API.

Provides typed access to all Profile operations.
"""

profile_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@profile_server.tool
@wrapped_fn_tool
def get_profile(
    profile_id: str,
    fields: list[str] = [],
) -> str:
    obj = Profile(profile_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@profile_server.tool
@wrapped_fn_tool
def get_picture(
    profile_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Profile(profile_id).get_picture(fields=fields, params=params)
