"""
Auto-generated MCP server for Facebook BidSchedule.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.bidschedule import BidSchedule
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-bidschedule")


# CRUD Operations


@mcp.tool()
async def get_bidschedule(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BidSchedule.

    Args:
        object_id: The ID of the BidSchedule
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BidSchedule(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
bidschedule_server = mcp
