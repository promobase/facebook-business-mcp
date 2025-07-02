"""
Auto-generated MCP server for Facebook CommerceMerchantSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.commercemerchantsettings import CommerceMerchantSettings
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-commercemerchantsettings")


# CRUD Operations


@mcp.tool()
async def get_commercemerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CommerceMerchantSettings.

    Args:
        object_id: The ID of the CommerceMerchantSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CommerceMerchantSettings(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_acknowledge_order_for_commercemerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Acknowledge Order for CommerceMerchantSettings.

    Args:
        object_id: The ID of the CommerceMerchantSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_acknowledge_order result
    """
    result = CommerceMerchantSettings(fbid=object_id).create_acknowledge_order(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_order_management_app_for_commercemerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Order Management App for CommerceMerchantSettings.

    Args:
        object_id: The ID of the CommerceMerchantSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_order_management_app result
    """
    result = CommerceMerchantSettings(fbid=object_id).create_order_management_app(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_shipping_profile_for_commercemerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Shipping Profile for CommerceMerchantSettings.

    Args:
        object_id: The ID of the CommerceMerchantSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_shipping_profile result
    """
    result = CommerceMerchantSettings(fbid=object_id).create_shipping_profile(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_commerce_orders_for_commercemerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Commerce Orders for CommerceMerchantSettings.

    Args:
        object_id: The ID of the CommerceMerchantSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_commerce_orders result
    """
    result = CommerceMerchantSettings(fbid=object_id).get_commerce_orders(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_commerce_payouts_for_commercemerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Commerce Payouts for CommerceMerchantSettings.

    Args:
        object_id: The ID of the CommerceMerchantSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_commerce_payouts result
    """
    result = CommerceMerchantSettings(fbid=object_id).get_commerce_payouts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_commerce_transactions_for_commercemerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Commerce Transactions for CommerceMerchantSettings.

    Args:
        object_id: The ID of the CommerceMerchantSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_commerce_transactions result
    """
    result = CommerceMerchantSettings(fbid=object_id).get_commerce_transactions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_order_management_apps_for_commercemerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Order Management Apps for CommerceMerchantSettings.

    Args:
        object_id: The ID of the CommerceMerchantSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_order_management_apps result
    """
    result = CommerceMerchantSettings(fbid=object_id).get_order_management_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_product_catalogs_for_commercemerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Product Catalogs for CommerceMerchantSettings.

    Args:
        object_id: The ID of the CommerceMerchantSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_product_catalogs result
    """
    result = CommerceMerchantSettings(fbid=object_id).get_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_returns_for_commercemerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Returns for CommerceMerchantSettings.

    Args:
        object_id: The ID of the CommerceMerchantSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_returns result
    """
    result = CommerceMerchantSettings(fbid=object_id).get_returns(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_setup_status_for_commercemerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Setup Status for CommerceMerchantSettings.

    Args:
        object_id: The ID of the CommerceMerchantSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_setup_status result
    """
    result = CommerceMerchantSettings(fbid=object_id).get_setup_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shipping_profiles_for_commercemerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Shipping Profiles for CommerceMerchantSettings.

    Args:
        object_id: The ID of the CommerceMerchantSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_shipping_profiles result
    """
    result = CommerceMerchantSettings(fbid=object_id).get_shipping_profiles(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shops_for_commercemerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Shops for CommerceMerchantSettings.

    Args:
        object_id: The ID of the CommerceMerchantSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_shops result
    """
    result = CommerceMerchantSettings(fbid=object_id).get_shops(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_tax_settings_for_commercemerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Tax Settings for CommerceMerchantSettings.

    Args:
        object_id: The ID of the CommerceMerchantSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_tax_settings result
    """
    result = CommerceMerchantSettings(fbid=object_id).get_tax_settings(
        fields=fields,
        params=params,
    )

    return result


# Export the server
commercemerchantsettings_server = mcp
