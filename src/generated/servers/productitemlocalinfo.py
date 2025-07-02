"""
Auto-generated MCP server for Facebook ProductItemLocalInfo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productitemlocalinfo import ProductItemLocalInfo
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productitemlocalinfo")


# CRUD Operations


@mcp.tool()
async def get_productitemlocalinfo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ProductItemLocalInfo.

    Args:
        object_id: The ID of the ProductItemLocalInfo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ProductItemLocalInfo(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productitemlocalinfo_server = mcp
