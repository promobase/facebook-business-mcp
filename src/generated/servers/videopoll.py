"""
Auto-generated MCP server for Facebook VideoPoll.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.videopoll import VideoPoll
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-videopoll")


# CRUD Operations


@mcp.tool()
async def get_videopoll(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a VideoPoll.

    Args:
        object_id: The ID of the VideoPoll
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = VideoPoll(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_videopoll(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a VideoPoll.

    Args:
        object_id: The ID of the VideoPoll
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = VideoPoll(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_poll_options_for_videopoll(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Poll Options for VideoPoll.

    Args:
        object_id: The ID of the VideoPoll
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_poll_options result
    """
    result = VideoPoll(fbid=object_id).get_poll_options(
        fields=fields,
        params=params,
    )

    return result


# Export the server
videopoll_server = mcp
