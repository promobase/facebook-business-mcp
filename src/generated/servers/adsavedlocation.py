"""
Auto-generated MCP server for Facebook AdSavedLocation.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsavedlocation import AdSavedLocation
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsavedlocation")


# CRUD Operations


@mcp.tool()
async def get_adsavedlocation(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdSavedLocation.

    Args:
        object_id: The ID of the AdSavedLocation
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdSavedLocation(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsavedlocation_server = mcp
