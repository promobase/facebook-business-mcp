"""
Auto-generated MCP server for Facebook CatalogWebsiteSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.catalogwebsitesettings import CatalogWebsiteSettings
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-catalogwebsitesettings")


# CRUD Operations


@mcp.tool()
async def get_catalogwebsitesettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CatalogWebsiteSettings.

    Args:
        object_id: The ID of the CatalogWebsiteSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CatalogWebsiteSettings(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
catalogwebsitesettings_server = mcp
