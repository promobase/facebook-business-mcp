"""
Auto-generated MCP server for Facebook ProductItem.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productitem import ProductItem
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productitem")


# CRUD Operations


@mcp.tool()
async def create_productitem(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a ProductItem.

    Args:
        object_id: The ID of the ProductItem
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = ProductItem(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_productitem(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a ProductItem.

    Args:
        object_id: The ID of the ProductItem
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = ProductItem(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_productitem(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ProductItem.

    Args:
        object_id: The ID of the ProductItem
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ProductItem(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_productitem(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a ProductItem.

    Args:
        object_id: The ID of the ProductItem
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = ProductItem(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_channels_to_integrity_status_for_productitem(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Channels To Integrity Status for ProductItem.

    Args:
        object_id: The ID of the ProductItem
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_channels_to_integrity_status result
    """
    result = ProductItem(fbid=object_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_override_details_for_productitem(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Override Details for ProductItem.

    Args:
        object_id: The ID of the ProductItem
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_override_details result
    """
    result = ProductItem(fbid=object_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_product_sets_for_productitem(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Product Sets for ProductItem.

    Args:
        object_id: The ID of the ProductItem
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_product_sets result
    """
    result = ProductItem(fbid=object_id).get_product_sets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_videos_metadata_for_productitem(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Videos Metadata for ProductItem.

    Args:
        object_id: The ID of the ProductItem
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_videos_metadata result
    """
    result = ProductItem(fbid=object_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productitem_server = mcp
