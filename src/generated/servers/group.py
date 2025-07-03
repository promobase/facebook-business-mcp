"""
Auto-generated MCP server for Facebook Group.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.group import Group
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-group")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    group_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_admin(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).create_admin(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_feed(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).create_feed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_group(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).create_group(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_live_video(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).create_live_video(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_member(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).create_member(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_photo(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).create_photo(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_video(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).create_video(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_admins(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).delete_admins(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_members(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).delete_members(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_albums(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).get_albums(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_docs(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).get_docs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_events(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).get_events(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_feed(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).get_feed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_files(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).get_files(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_groups(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).get_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_live_videos(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).get_live_videos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_opted_in_members(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).get_opted_in_members(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_picture(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).get_picture(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_videos(
    group_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Group(fbid=group_id).get_videos(
        fields=fields,
        params=params,
    )

    return result


# Export the server
group_server = mcp
