"""
Auto-generated MCP server for Facebook VideoList.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.videolist import VideoList
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-videolist")


# CRUD Operations


@mcp.tool()
async def get_videolist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a VideoList.

    Args:
        object_id: The ID of the VideoList
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = VideoList(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_videos_for_videolist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Videos for VideoList.

    Args:
        object_id: The ID of the VideoList
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_videos result
    """
    result = VideoList(fbid=object_id).get_videos(
        fields=fields,
        params=params,
    )

    return result


# Export the server
videolist_server = mcp
