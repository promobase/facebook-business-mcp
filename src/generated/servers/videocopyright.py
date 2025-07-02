"""
Auto-generated MCP server for Facebook VideoCopyright.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.videocopyright import VideoCopyright
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-videocopyright")


# CRUD Operations


@mcp.tool()
async def get_videocopyright(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a VideoCopyright.

    Args:
        object_id: The ID of the VideoCopyright
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = VideoCopyright(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_videocopyright(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a VideoCopyright.

    Args:
        object_id: The ID of the VideoCopyright
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = VideoCopyright(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_update_records_for_videocopyright(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Update Records for VideoCopyright.

    Args:
        object_id: The ID of the VideoCopyright
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_update_records result
    """
    result = VideoCopyright(fbid=object_id).get_update_records(
        fields=fields,
        params=params,
    )

    return result


# Export the server
videocopyright_server = mcp
