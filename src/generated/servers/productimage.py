"""
Auto-generated MCP server for Facebook ProductImage.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productimage import ProductImage
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productimage")


# CRUD Operations


@mcp.tool()
async def get_productimage(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ProductImage.

    Args:
        object_id: The ID of the ProductImage
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ProductImage(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productimage_server = mcp
