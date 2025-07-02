"""
Auto-generated MCP server for Facebook BrandSafetyDownloadable.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.brandsafetydownloadable import BrandSafetyDownloadable
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-brandsafetydownloadable")


# CRUD Operations


@mcp.tool()
async def get_brandsafetydownloadable(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BrandSafetyDownloadable.

    Args:
        object_id: The ID of the BrandSafetyDownloadable
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BrandSafetyDownloadable(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
brandsafetydownloadable_server = mcp
