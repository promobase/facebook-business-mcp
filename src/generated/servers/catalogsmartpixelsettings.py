"""
Auto-generated MCP server for Facebook CatalogSmartPixelSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.catalogsmartpixelsettings import CatalogSmartPixelSettings
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-catalogsmartpixelsettings")


# CRUD Operations


@mcp.tool()
async def get_catalogsmartpixelsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CatalogSmartPixelSettings.

    Args:
        object_id: The ID of the CatalogSmartPixelSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CatalogSmartPixelSettings(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
catalogsmartpixelsettings_server = mcp
