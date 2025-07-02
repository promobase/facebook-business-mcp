"""VideoCopyright MCP Server."""

from typing import Any

from facebook_business.adobjects.videocopyright import VideoCopyright
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookVideoCopyright"
instructions = """
VideoCopyright MCP Server for Facebook Business API.

Provides typed access to all VideoCopyright operations.
"""

videocopyright_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@videocopyright_server.tool
@wrapped_fn_tool
def get_videocopyright(
    videocopyright_id: str,
    fields: list[str] = [],
) -> str:
    obj = VideoCopyright(videocopyright_id)
    return obj.api_get(fields=fields)


@videocopyright_server.tool
@wrapped_fn_tool
def update_videocopyright(
    videocopyright_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return VideoCopyright(videocopyright_id).api_update(fields=fields, params=params)


# ---- Edge Methods (1) ----
@videocopyright_server.tool
@wrapped_fn_tool
def get_update_records(
    videocopyright_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return VideoCopyright(videocopyright_id).get_update_records(fields=fields, params=params)
