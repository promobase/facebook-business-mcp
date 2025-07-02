"""
Auto-generated MCP server for Facebook EventTicketTier.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.eventtickettier import EventTicketTier
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-eventtickettier")


# CRUD Operations


@mcp.tool()
async def get_eventtickettier(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a EventTicketTier.

    Args:
        object_id: The ID of the EventTicketTier
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = EventTicketTier(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
eventtickettier_server = mcp
