"""
Auto-generated MCP server for Facebook Shop.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.shop import Shop
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-shop")


# CRUD Operations


@mcp.tool()
async def get_shop(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Shop.

    Args:
        object_id: The ID of the Shop
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Shop(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
shop_server = mcp
