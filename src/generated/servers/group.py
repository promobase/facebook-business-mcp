"""
Auto-generated MCP server for Facebook Group.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.group import Group
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-group")


# CRUD Operations


@mcp.tool()
async def create_group(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_admin_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).create_admin(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_feed_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).create_feed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_group_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).create_group(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_live_video_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).create_live_video(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_member_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).create_member(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_photo_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).create_photo(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_video_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).create_video(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_admins_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).delete_admins(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_members_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).delete_members(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_albums_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).get_albums(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_docs_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).get_docs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_events_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).get_events(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_feed_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).get_feed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_files_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).get_files(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_groups_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).get_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_live_videos_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).get_live_videos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_opted_in_members_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).get_opted_in_members(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_picture_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).get_picture(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_videos_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Group(fbid=object_id).get_videos(
        fields=fields,
        params=params,
    )

    return result


# Export the server
group_server = mcp
