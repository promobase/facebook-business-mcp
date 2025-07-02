"""
Auto-generated MCP server for Facebook LifeEvent.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.lifeevent import LifeEvent
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-lifeevent")


# CRUD Operations


@mcp.tool()
async def get_lifeevent(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a LifeEvent.

    Args:
        object_id: The ID of the LifeEvent
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = LifeEvent(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_likes_for_lifeevent(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Likes for LifeEvent.

    Args:
        object_id: The ID of the LifeEvent
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_likes result
    """
    result = LifeEvent(fbid=object_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


# Export the server
lifeevent_server = mcp
