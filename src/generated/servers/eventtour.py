"""
Auto-generated MCP server for Facebook EventTour.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.eventtour import EventTour
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-eventtour")


# CRUD Operations


@mcp.tool()
async def get_eventtour(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a EventTour.

    Args:
        object_id: The ID of the EventTour
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = EventTour(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
eventtour_server = mcp
