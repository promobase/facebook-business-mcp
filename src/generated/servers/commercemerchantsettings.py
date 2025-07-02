"""
Auto-generated MCP server for Facebook CommerceMerchantSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.commercemerchantsettings import CommerceMerchantSettings
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-commercemerchantsettings")


# CRUD Operations


@mcp.tool()
async def create_commercemerchantsettings(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CommerceMerchantSettings(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_commercemerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CommerceMerchantSettings(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_commercemerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CommerceMerchantSettings(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_commercemerchantsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CommerceMerchantSettings(fbid=object_id).api_update(
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
    result = CommerceMerchantSettings(fbid=object_id).get_tax_settings(
        fields=fields,
        params=params,
    )

    return result


# Export the server
commercemerchantsettings_server = mcp
