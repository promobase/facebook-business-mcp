"""
Auto-generated MCP server for Facebook CatalogItemOverride.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.catalogitemoverride import CatalogItemOverride
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-catalogitemoverride")


# CRUD Operations


@mcp.tool()
async def get_catalogitemoverride(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CatalogItemOverride.

    Args:
        object_id: The ID of the CatalogItemOverride
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CatalogItemOverride(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
catalogitemoverride_server = mcp
