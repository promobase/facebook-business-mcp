"""
Auto-generated MCP server for Facebook BusinessUser.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessuser import BusinessUser
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessuser")


# CRUD Operations


@mcp.tool()
async def create_businessuser(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a BusinessUser.

    Args:
        object_id: The ID of the BusinessUser
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = BusinessUser(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_businessuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a BusinessUser.

    Args:
        object_id: The ID of the BusinessUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = BusinessUser(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_businessuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BusinessUser.

    Args:
        object_id: The ID of the BusinessUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BusinessUser(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_businessuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a BusinessUser.

    Args:
        object_id: The ID of the BusinessUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = BusinessUser(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_assigned_ad_accounts_for_businessuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Assigned Ad Accounts for BusinessUser.

    Args:
        object_id: The ID of the BusinessUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_assigned_ad_accounts result
    """
    result = BusinessUser(fbid=object_id).get_assigned_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_business_asset_groups_for_businessuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Assigned Business Asset Groups for BusinessUser.

    Args:
        object_id: The ID of the BusinessUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_assigned_business_asset_groups result
    """
    result = BusinessUser(fbid=object_id).get_assigned_business_asset_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_pages_for_businessuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Assigned Pages for BusinessUser.

    Args:
        object_id: The ID of the BusinessUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_assigned_pages result
    """
    result = BusinessUser(fbid=object_id).get_assigned_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_product_catalogs_for_businessuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Assigned Product Catalogs for BusinessUser.

    Args:
        object_id: The ID of the BusinessUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_assigned_product_catalogs result
    """
    result = BusinessUser(fbid=object_id).get_assigned_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessuser_server = mcp
