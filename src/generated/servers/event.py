"""
Auto-generated MCP server for Facebook Event.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.event import Event
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-event")


# CRUD Operations


@mcp.tool()
async def get_event(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Event.

    Args:
        object_id: The ID of the Event
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Event(fbid=object_id).api_get(
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
    """
    Create Live Video for Event.

    Args:
        object_id: The ID of the Event
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_live_video result
    """
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
    """
    Get Comments for Event.

    Args:
        object_id: The ID of the Event
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_comments result
    """
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
    """
    Get Feed for Event.

    Args:
        object_id: The ID of the Event
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_feed result
    """
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
    """
    Get Live Videos for Event.

    Args:
        object_id: The ID of the Event
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_live_videos result
    """
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
    """
    Get Photos for Event.

    Args:
        object_id: The ID of the Event
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_photos result
    """
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
    """
    Get Picture for Event.

    Args:
        object_id: The ID of the Event
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_picture result
    """
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
    """
    Get Posts for Event.

    Args:
        object_id: The ID of the Event
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_posts result
    """
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
    """
    Get Roles for Event.

    Args:
        object_id: The ID of the Event
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_roles result
    """
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
    """
    Get Ticket Tiers for Event.

    Args:
        object_id: The ID of the Event
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ticket_tiers result
    """
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
    """
    Get Videos for Event.

    Args:
        object_id: The ID of the Event
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_videos result
    """
    result = Event(fbid=object_id).get_videos(
        fields=fields,
        params=params,
    )

    return result


# Export the server
event_server = mcp
