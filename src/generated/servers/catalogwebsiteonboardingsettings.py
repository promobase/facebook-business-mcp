"""
Auto-generated MCP server for Facebook CatalogWebsiteOnboardingSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.catalogwebsiteonboardingsettings import (
    CatalogWebsiteOnboardingSettings,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-catalogwebsiteonboardingsettings")


# CRUD Operations


@mcp.tool()
async def get_catalogwebsiteonboardingsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CatalogWebsiteOnboardingSettings.

    Args:
        object_id: The ID of the CatalogWebsiteOnboardingSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CatalogWebsiteOnboardingSettings(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
catalogwebsiteonboardingsettings_server = mcp
