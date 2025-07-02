"""
Auto-generated MCP server for Facebook BusinessAssetGroup.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessassetgroup import BusinessAssetGroup
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessassetgroup")


# CRUD Operations


@mcp.tool()
async def get_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BusinessAssetGroup(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = BusinessAssetGroup(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_assigned_user_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Assigned User for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_assigned_user result
    """
    result = BusinessAssetGroup(fbid=object_id).create_assigned_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_ad_account_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Contained Ad Account for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_contained_ad_account result
    """
    result = BusinessAssetGroup(fbid=object_id).create_contained_ad_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_application_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Contained Application for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_contained_application result
    """
    result = BusinessAssetGroup(fbid=object_id).create_contained_application(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_custom_conversion_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Contained Custom Conversion for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_contained_custom_conversion result
    """
    result = BusinessAssetGroup(fbid=object_id).create_contained_custom_conversion(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_instagram_account_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Contained Instagram Account for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_contained_instagram_account result
    """
    result = BusinessAssetGroup(fbid=object_id).create_contained_instagram_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_page_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Contained Page for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_contained_page result
    """
    result = BusinessAssetGroup(fbid=object_id).create_contained_page(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_pixel_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Contained Pixel for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_contained_pixel result
    """
    result = BusinessAssetGroup(fbid=object_id).create_contained_pixel(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_contained_product_catalog_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Contained Product Catalog for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_contained_product_catalog result
    """
    result = BusinessAssetGroup(fbid=object_id).create_contained_product_catalog(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_assigned_users_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Assigned Users for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_assigned_users result
    """
    result = BusinessAssetGroup(fbid=object_id).delete_assigned_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_ad_accounts_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Contained Ad Accounts for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_contained_ad_accounts result
    """
    result = BusinessAssetGroup(fbid=object_id).delete_contained_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_applications_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Contained Applications for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_contained_applications result
    """
    result = BusinessAssetGroup(fbid=object_id).delete_contained_applications(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_custom_conversions_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Contained Custom Conversions for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_contained_custom_conversions result
    """
    result = BusinessAssetGroup(fbid=object_id).delete_contained_custom_conversions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_instagram_accounts_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Contained Instagram Accounts for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_contained_instagram_accounts result
    """
    result = BusinessAssetGroup(fbid=object_id).delete_contained_instagram_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_pages_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Contained Pages for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_contained_pages result
    """
    result = BusinessAssetGroup(fbid=object_id).delete_contained_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_pixels_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Contained Pixels for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_contained_pixels result
    """
    result = BusinessAssetGroup(fbid=object_id).delete_contained_pixels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_contained_product_catalogs_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Contained Product Catalogs for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_contained_product_catalogs result
    """
    result = BusinessAssetGroup(fbid=object_id).delete_contained_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_users_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Assigned Users for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_assigned_users result
    """
    result = BusinessAssetGroup(fbid=object_id).get_assigned_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_ad_accounts_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Contained Ad Accounts for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_contained_ad_accounts result
    """
    result = BusinessAssetGroup(fbid=object_id).get_contained_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_applications_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Contained Applications for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_contained_applications result
    """
    result = BusinessAssetGroup(fbid=object_id).get_contained_applications(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_custom_conversions_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Contained Custom Conversions for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_contained_custom_conversions result
    """
    result = BusinessAssetGroup(fbid=object_id).get_contained_custom_conversions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_instagram_accounts_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Contained Instagram Accounts for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_contained_instagram_accounts result
    """
    result = BusinessAssetGroup(fbid=object_id).get_contained_instagram_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_pages_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Contained Pages for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_contained_pages result
    """
    result = BusinessAssetGroup(fbid=object_id).get_contained_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_pixels_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Contained Pixels for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_contained_pixels result
    """
    result = BusinessAssetGroup(fbid=object_id).get_contained_pixels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_contained_product_catalogs_for_businessassetgroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Contained Product Catalogs for BusinessAssetGroup.

    Args:
        object_id: The ID of the BusinessAssetGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_contained_product_catalogs result
    """
    result = BusinessAssetGroup(fbid=object_id).get_contained_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessassetgroup_server = mcp
