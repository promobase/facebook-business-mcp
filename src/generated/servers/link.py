"""
Auto-generated MCP server for Facebook Link.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.link import Link
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-link")


# CRUD Operations


@mcp.tool()
async def get_link(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Link.

    Args:
        object_id: The ID of the Link
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Link(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_comment_for_link(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Comment for Link.

    Args:
        object_id: The ID of the Link
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_comment result
    """
    result = Link(fbid=object_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_likes_for_link(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Likes for Link.

    Args:
        object_id: The ID of the Link
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_likes result
    """
    result = Link(fbid=object_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


# Export the server
link_server = mcp
