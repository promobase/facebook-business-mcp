"""
Auto-generated MCP server for Facebook Event.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.event import Event
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-event")


# CRUD Operations


@mcp.tool()
async def create_event(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Event(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_event(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Event(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_event(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Event(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_event(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Event(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_live_video_for_event(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Event(fbid=object_id).create_live_video(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_comments_for_event(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Event(fbid=object_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_feed_for_event(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Event(fbid=object_id).get_feed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_live_videos_for_event(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Event(fbid=object_id).get_live_videos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_photos_for_event(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Event(fbid=object_id).get_photos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_picture_for_event(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Event(fbid=object_id).get_picture(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_posts_for_event(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Event(fbid=object_id).get_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_roles_for_event(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Event(fbid=object_id).get_roles(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ticket_tiers_for_event(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Event(fbid=object_id).get_ticket_tiers(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_videos_for_event(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Event(fbid=object_id).get_videos(
        fields=fields,
        params=params,
    )

    return result


# Export the server
event_server = mcp
