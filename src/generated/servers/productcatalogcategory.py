"""
Auto-generated MCP server for Facebook ProductCatalogCategory.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productcatalogcategory import ProductCatalogCategory
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productcatalogcategory")


# CRUD Operations


@mcp.tool()
async def create_productcatalogcategory(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a ProductCatalogCategory.

    Args:
        object_id: The ID of the ProductCatalogCategory
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = ProductCatalogCategory(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


# Export the server
productcatalogcategory_server = mcp
