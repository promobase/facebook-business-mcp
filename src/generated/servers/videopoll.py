"""VideoPoll MCP Server."""

from typing import Any

from facebook_business.adobjects.videopoll import VideoPoll
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookVideoPoll"
instructions = """
VideoPoll MCP Server for Facebook Business API.

Provides typed access to all VideoPoll operations.
"""

videopoll_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@videopoll_server.tool
@wrapped_fn_tool
def get_videopoll(
    videopoll_id: str,
    fields: list[str] = [],
) -> str:
    obj = VideoPoll(videopoll_id)
    return obj.api_get(fields=fields)


@videopoll_server.tool
@wrapped_fn_tool
def update_videopoll(
    videopoll_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return VideoPoll(videopoll_id).api_update(fields=fields, params=params)


# ---- Edge Methods (1) ----
@videopoll_server.tool
@wrapped_fn_tool
def get_poll_options(
    videopoll_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return VideoPoll(videopoll_id).get_poll_options(fields=fields, params=params)
