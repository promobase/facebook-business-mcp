"""
Auto-generated MCP server for Facebook ProductSetUsage.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productsetusage import ProductSetUsage
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productsetusage")


# CRUD Operations


@mcp.tool()
async def get_productsetusage(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ProductSetUsage.

    Args:
        object_id: The ID of the ProductSetUsage
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ProductSetUsage(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productsetusage_server = mcp
