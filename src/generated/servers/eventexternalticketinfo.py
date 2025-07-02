"""
Auto-generated MCP server for Facebook EventExternalTicketInfo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.eventexternalticketinfo import EventExternalTicketInfo
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-eventexternalticketinfo")


# CRUD Operations


@mcp.tool()
async def get_eventexternalticketinfo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a EventExternalTicketInfo.

    Args:
        object_id: The ID of the EventExternalTicketInfo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = EventExternalTicketInfo(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
eventexternalticketinfo_server = mcp
