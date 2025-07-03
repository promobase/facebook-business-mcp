"""
Auto-generated MCP server for Facebook Event.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.event import Event
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-event")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    event_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Event(fbid=event_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    event_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Event(fbid=event_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    event_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Event(fbid=event_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    event_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Event(fbid=event_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_live_video(
    event_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Event(fbid=event_id).create_live_video(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_comments(
    event_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Event(fbid=event_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_feed(
    event_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Event(fbid=event_id).get_feed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_live_videos(
    event_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Event(fbid=event_id).get_live_videos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_photos(
    event_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Event(fbid=event_id).get_photos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_picture(
    event_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Event(fbid=event_id).get_picture(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_posts(
    event_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Event(fbid=event_id).get_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_roles(
    event_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Event(fbid=event_id).get_roles(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ticket_tiers(
    event_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Event(fbid=event_id).get_ticket_tiers(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_videos(
    event_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Event(fbid=event_id).get_videos(
        fields=fields,
        params=params,
    )

    return result


# Export the server
event_server = mcp
