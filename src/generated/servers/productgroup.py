"""
Auto-generated MCP server for Facebook ProductGroup.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productgroup import ProductGroup
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productgroup")


# CRUD Operations


@mcp.tool()
async def create_productgroup(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a ProductGroup.

    Args:
        object_id: The ID of the ProductGroup
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = ProductGroup(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_productgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a ProductGroup.

    Args:
        object_id: The ID of the ProductGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = ProductGroup(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_productgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ProductGroup.

    Args:
        object_id: The ID of the ProductGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ProductGroup(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_productgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a ProductGroup.

    Args:
        object_id: The ID of the ProductGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = ProductGroup(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_product_for_productgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Product for ProductGroup.

    Args:
        object_id: The ID of the ProductGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_product result
    """
    result = ProductGroup(fbid=object_id).create_product(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_products_for_productgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Products for ProductGroup.

    Args:
        object_id: The ID of the ProductGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_products result
    """
    result = ProductGroup(fbid=object_id).get_products(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productgroup_server = mcp
