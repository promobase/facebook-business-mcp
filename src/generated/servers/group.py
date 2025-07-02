"""Group MCP Server."""

from typing import Any

from facebook_business.adobjects.group import Group
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookGroup"
instructions = """
Group MCP Server for Facebook Business API.

Provides typed access to all Group operations.
"""

group_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@group_server.tool
@wrapped_fn_tool
def get_group(
    group_id: str,
    fields: list[str] = [],
) -> str:
    obj = Group(group_id)
    return obj.api_get(fields=fields)


@group_server.tool
@wrapped_fn_tool
def update_group(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Group(group_id).api_update(fields=fields, params=params)


# ---- Edge Methods (19) ----
@group_server.tool
@wrapped_fn_tool
def delete_admins(
    group_id: str,
    params: dict[str, Any] = {},
):
    return Group(group_id).delete_admins(params=params)


@group_server.tool
@wrapped_fn_tool
def create_admin(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Group(group_id).create_admin(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def get_albums(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Group(group_id).get_albums(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def get_docs(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Group(group_id).get_docs(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def get_events(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Group(group_id).get_events(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def get_feed(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Group(group_id).get_feed(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def create_feed(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Group(group_id).create_feed(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def get_files(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Group(group_id).get_files(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def get_groups(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Group(group_id).get_groups(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def create_group(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Group(group_id).create_group(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def get_live_videos(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Group(group_id).get_live_videos(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def create_live_video(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Group(group_id).create_live_video(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def delete_members(
    group_id: str,
    params: dict[str, Any] = {},
):
    return Group(group_id).delete_members(params=params)


@group_server.tool
@wrapped_fn_tool
def create_member(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Group(group_id).create_member(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def get_opted_in_members(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Group(group_id).get_opted_in_members(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def create_photo(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Group(group_id).create_photo(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def get_picture(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Group(group_id).get_picture(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def get_videos(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Group(group_id).get_videos(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def create_video(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Group(group_id).create_video(fields=fields, params=params)
