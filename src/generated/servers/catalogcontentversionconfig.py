"""
Auto-generated MCP server for Facebook CatalogContentVersionConfig.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.catalogcontentversionconfig import CatalogContentVersionConfig
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-catalogcontentversionconfig")


# CRUD Operations


@mcp.tool()
async def get_catalogcontentversionconfig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CatalogContentVersionConfig.

    Args:
        object_id: The ID of the CatalogContentVersionConfig
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CatalogContentVersionConfig(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
catalogcontentversionconfig_server = mcp
