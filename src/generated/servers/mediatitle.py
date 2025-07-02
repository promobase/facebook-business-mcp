"""MediaTitle MCP Server."""

from typing import Any

from facebook_business.adobjects.mediatitle import MediaTitle
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookMediaTitle"
instructions = """
MediaTitle MCP Server for Facebook Business API.

Provides typed access to all MediaTitle operations.
"""

mediatitle_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@mediatitle_server.tool
@wrapped_fn_tool
def get_mediatitle(
    mediatitle_id: str,
    fields: list[str] = [],
) -> str:
    obj = MediaTitle(mediatitle_id)
    return obj.api_get(fields=fields)


@mediatitle_server.tool
@wrapped_fn_tool
def update_mediatitle(
    mediatitle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return MediaTitle(mediatitle_id).api_update(fields=fields, params=params)


@mediatitle_server.tool
@wrapped_fn_tool
def delete_mediatitle(
    mediatitle_id: str,
) -> str:
    return MediaTitle(mediatitle_id).api_delete()


# ---- Edge Methods (3) ----
@mediatitle_server.tool
@wrapped_fn_tool
def get_channels_to_integrity_status(
    mediatitle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return MediaTitle(mediatitle_id).get_channels_to_integrity_status(fields=fields, params=params)


@mediatitle_server.tool
@wrapped_fn_tool
def get_override_details(
    mediatitle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return MediaTitle(mediatitle_id).get_override_details(fields=fields, params=params)


@mediatitle_server.tool
@wrapped_fn_tool
def get_videos_metadata(
    mediatitle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return MediaTitle(mediatitle_id).get_videos_metadata(fields=fields, params=params)
