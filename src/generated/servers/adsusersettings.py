"""
Auto-generated MCP server for Facebook AdsUserSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsusersettings import AdsUserSettings
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsusersettings")


# CRUD Operations


@mcp.tool()
async def get_adsusersettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdsUserSettings.

    Args:
        object_id: The ID of the AdsUserSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdsUserSettings(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsusersettings_server = mcp
