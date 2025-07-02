"""
Auto-generated MCP server for Facebook EventRegistrationSetting.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.eventregistrationsetting import EventRegistrationSetting
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-eventregistrationsetting")


# CRUD Operations


@mcp.tool()
async def get_eventregistrationsetting(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a EventRegistrationSetting.

    Args:
        object_id: The ID of the EventRegistrationSetting
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = EventRegistrationSetting(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
eventregistrationsetting_server = mcp
