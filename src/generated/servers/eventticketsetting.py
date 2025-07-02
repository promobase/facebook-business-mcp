"""
Auto-generated MCP server for Facebook EventTicketSetting.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.eventticketsetting import EventTicketSetting
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-eventticketsetting")


# CRUD Operations


@mcp.tool()
async def get_eventticketsetting(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a EventTicketSetting.

    Args:
        object_id: The ID of the EventTicketSetting
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = EventTicketSetting(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
eventticketsetting_server = mcp
