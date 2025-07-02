"""LiveVideo MCP Server."""

from typing import Any

from facebook_business.adobjects.livevideo import LiveVideo
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLiveVideo"
instructions = """
LiveVideo MCP Server for Facebook Business API.

Provides typed access to all LiveVideo operations.
"""

livevideo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@livevideo_server.tool
@wrapped_fn_tool
def get_livevideo(
    livevideo_id: str,
    fields: list[str] = [],
) -> str:
    obj = LiveVideo(livevideo_id)
    return obj.api_get(fields=fields)


@livevideo_server.tool
@wrapped_fn_tool
def update_livevideo(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return LiveVideo(livevideo_id).api_update(fields=fields, params=params)


@livevideo_server.tool
@wrapped_fn_tool
def delete_livevideo(
    livevideo_id: str,
) -> str:
    return LiveVideo(livevideo_id).api_delete()


# ---- Edge Methods (9) ----
@livevideo_server.tool
@wrapped_fn_tool
def get_blocked_users(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return LiveVideo(livevideo_id).get_blocked_users(fields=fields, params=params)


@livevideo_server.tool
@wrapped_fn_tool
def get_comments(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return LiveVideo(livevideo_id).get_comments(fields=fields, params=params)


@livevideo_server.tool
@wrapped_fn_tool
def get_crosspost_shared_pages(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return LiveVideo(livevideo_id).get_crosspost_shared_pages(fields=fields, params=params)


@livevideo_server.tool
@wrapped_fn_tool
def get_crossposted_broadcasts(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return LiveVideo(livevideo_id).get_crossposted_broadcasts(fields=fields, params=params)


@livevideo_server.tool
@wrapped_fn_tool
def get_errors(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return LiveVideo(livevideo_id).get_errors(fields=fields, params=params)


@livevideo_server.tool
@wrapped_fn_tool
def create_input_stream(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return LiveVideo(livevideo_id).create_input_stream(fields=fields, params=params)


@livevideo_server.tool
@wrapped_fn_tool
def get_polls(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return LiveVideo(livevideo_id).get_polls(fields=fields, params=params)


@livevideo_server.tool
@wrapped_fn_tool
def create_poll(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return LiveVideo(livevideo_id).create_poll(fields=fields, params=params)


@livevideo_server.tool
@wrapped_fn_tool
def get_reactions(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return LiveVideo(livevideo_id).get_reactions(fields=fields, params=params)
