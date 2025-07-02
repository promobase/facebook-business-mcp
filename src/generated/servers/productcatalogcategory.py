"""
Auto-generated MCP server for Facebook ProductCatalogCategory.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productcatalogcategory import ProductCatalogCategory
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
    result = ProductCatalogCategory(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_productcatalogcategory(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductCatalogCategory(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_productcatalogcategory(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductCatalogCategory(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_productcatalogcategory(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductCatalogCategory(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productcatalogcategory_server = mcp
