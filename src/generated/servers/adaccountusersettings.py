"""
Auto-generated MCP server for Facebook AdAccountUserSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adaccountusersettings import AdAccountUserSettings
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adaccountusersettings")


# CRUD Operations


@mcp.tool()
async def get_adaccountusersettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdAccountUserSettings.

    Args:
        object_id: The ID of the AdAccountUserSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdAccountUserSettings(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adaccountusersettings_server = mcp
