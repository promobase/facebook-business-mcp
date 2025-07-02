"""
Auto-generated MCP server for Facebook RTBDynamicPost.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.rtbdynamicpost import RTBDynamicPost
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-rtbdynamicpost")


# CRUD Operations


@mcp.tool()
async def get_rtbdynamicpost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a RTBDynamicPost.

    Args:
        object_id: The ID of the RTBDynamicPost
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = RTBDynamicPost(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_comments_for_rtbdynamicpost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Comments for RTBDynamicPost.

    Args:
        object_id: The ID of the RTBDynamicPost
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_comments result
    """
    result = RTBDynamicPost(fbid=object_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_likes_for_rtbdynamicpost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Likes for RTBDynamicPost.

    Args:
        object_id: The ID of the RTBDynamicPost
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_likes result
    """
    result = RTBDynamicPost(fbid=object_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


# Export the server
rtbdynamicpost_server = mcp
