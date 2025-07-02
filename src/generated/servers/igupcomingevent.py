"""
Auto-generated MCP server for Facebook IGUpcomingEvent.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igupcomingevent import IGUpcomingEvent
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-igupcomingevent")


# CRUD Operations


@mcp.tool()
async def get_igupcomingevent(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a IGUpcomingEvent.

    Args:
        object_id: The ID of the IGUpcomingEvent
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = IGUpcomingEvent(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_igupcomingevent(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a IGUpcomingEvent.

    Args:
        object_id: The ID of the IGUpcomingEvent
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = IGUpcomingEvent(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igupcomingevent_server = mcp
