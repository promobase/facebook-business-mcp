"""RTBDynamicPost MCP Server."""

from typing import Any

from facebook_business.adobjects.rtbdynamicpost import RTBDynamicPost
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookRTBDynamicPost"
instructions = """
RTBDynamicPost MCP Server for Facebook Business API.

Provides typed access to all RTBDynamicPost operations.
"""

rtbdynamicpost_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@rtbdynamicpost_server.tool
@wrapped_fn_tool
def get_rtbdynamicpost(
    rtbdynamicpost_id: str,
    fields: list[str] = [],
) -> str:
    obj = RTBDynamicPost(rtbdynamicpost_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (2) ----
@rtbdynamicpost_server.tool
@wrapped_fn_tool
def get_comments(
    rtbdynamicpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return RTBDynamicPost(rtbdynamicpost_id).get_comments(fields=fields, params=params)


@rtbdynamicpost_server.tool
@wrapped_fn_tool
def get_likes(
    rtbdynamicpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return RTBDynamicPost(rtbdynamicpost_id).get_likes(fields=fields, params=params)
