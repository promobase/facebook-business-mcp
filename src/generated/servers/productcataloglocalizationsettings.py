"""
Auto-generated MCP server for Facebook ProductCatalogLocalizationSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productcataloglocalizationsettings import (
    ProductCatalogLocalizationSettings,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productcataloglocalizationsettings")


# CRUD Operations


@mcp.tool()
async def get_productcataloglocalizationsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ProductCatalogLocalizationSettings.

    Args:
        object_id: The ID of the ProductCatalogLocalizationSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ProductCatalogLocalizationSettings(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productcataloglocalizationsettings_server = mcp
