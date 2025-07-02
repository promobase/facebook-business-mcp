"""AdVideo MCP Server."""

from typing import Any

from facebook_business.adobjects.advideo import AdVideo
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdVideo"
instructions = """
AdVideo MCP Server for Facebook Business API.

Provides typed access to all AdVideo operations.
"""

advideo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@advideo_server.tool
@wrapped_fn_tool
def get_advideo(
    advideo_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdVideo(advideo_id)
    return obj.api_get(fields=fields)


@advideo_server.tool
@wrapped_fn_tool
def update_advideo(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdVideo(advideo_id).api_update(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def delete_advideo(
    advideo_id: str,
) -> str:
    return AdVideo(advideo_id).api_delete()


# ---- Edge Methods (9) ----
@advideo_server.tool
@wrapped_fn_tool
def create_cap_t_i_on(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdVideo(advideo_id).create_cap_t_i_on(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def create_collaborator(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdVideo(advideo_id).create_collaborator(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def get_comments(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdVideo(advideo_id).get_comments(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def create_comment(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdVideo(advideo_id).create_comment(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def create_gaming_clip_create(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdVideo(advideo_id).create_gaming_clip_create(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def create_like(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdVideo(advideo_id).create_like(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def create_poll(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdVideo(advideo_id).create_poll(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def create_thumbnail(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdVideo(advideo_id).create_thumbnail(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def get_video_insights(
    advideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdVideo(advideo_id).get_video_insights(fields=fields, params=params)
