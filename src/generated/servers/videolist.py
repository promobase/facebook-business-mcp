"""
Auto-generated MCP server for Facebook VideoList.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.videolist import VideoList
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-videolist")


# CRUD Operations


@mcp.tool()
async def api_create_videolist(
    videolist_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = VideoList(fbid=videolist_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_videolist(
    videolist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = VideoList(fbid=videolist_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_videolist(
    videolist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = VideoList(fbid=videolist_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_videolist(
    videolist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = VideoList(fbid=videolist_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_videos(
    videolist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = VideoList(fbid=videolist_id).get_videos(
        fields=fields,
        params=params,
    )

    return result


# Export the server
videolist_server = mcp
