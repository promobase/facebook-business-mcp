"""
Auto-generated MCP server for Facebook WifiInformation.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.wifiinformation import WifiInformation
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-wifiinformation")


# CRUD Operations


@mcp.tool()
async def get_wifiinformation(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a WifiInformation.

    Args:
        object_id: The ID of the WifiInformation
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = WifiInformation(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
wifiinformation_server = mcp
