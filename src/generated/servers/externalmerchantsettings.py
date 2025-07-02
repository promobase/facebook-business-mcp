"""
Auto-generated MCP server for Facebook ExternalMerchantSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.externalmerchantsettings import ExternalMerchantSettings
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-externalmerchantsettings")


# CRUD Operations


@mcp.tool()
async def get_externalmerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ExternalMerchantSettings.

    Args:
        object_id: The ID of the ExternalMerchantSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ExternalMerchantSettings(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
externalmerchantsettings_server = mcp
