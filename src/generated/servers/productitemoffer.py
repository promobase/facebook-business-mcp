"""
Auto-generated MCP server for Facebook ProductItemOffer.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productitemoffer import ProductItemOffer
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productitemoffer")


# CRUD Operations


@mcp.tool()
async def get_productitemoffer(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ProductItemOffer.

    Args:
        object_id: The ID of the ProductItemOffer
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ProductItemOffer(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productitemoffer_server = mcp
