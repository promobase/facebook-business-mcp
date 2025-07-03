"""
Auto-generated MCP server for Facebook CommerceMerchantSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.commercemerchantsettings import CommerceMerchantSettings
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-commercemerchantsettings")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    commercemerchantsettings_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceMerchantSettings(fbid=commercemerchantsettings_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceMerchantSettings(fbid=commercemerchantsettings_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceMerchantSettings(fbid=commercemerchantsettings_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceMerchantSettings(fbid=commercemerchantsettings_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_acknowledge_order(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceMerchantSettings(fbid=commercemerchantsettings_id).create_acknowledge_order(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_order_management_app(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceMerchantSettings(fbid=commercemerchantsettings_id).create_order_management_app(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_shipping_profile(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceMerchantSettings(fbid=commercemerchantsettings_id).create_shipping_profile(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_commerce_orders(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceMerchantSettings(fbid=commercemerchantsettings_id).get_commerce_orders(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_commerce_payouts(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceMerchantSettings(fbid=commercemerchantsettings_id).get_commerce_payouts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_commerce_transactions(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceMerchantSettings(fbid=commercemerchantsettings_id).get_commerce_transactions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_order_management_apps(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceMerchantSettings(fbid=commercemerchantsettings_id).get_order_management_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_product_catalogs(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceMerchantSettings(fbid=commercemerchantsettings_id).get_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_returns(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceMerchantSettings(fbid=commercemerchantsettings_id).get_returns(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_setup_status(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceMerchantSettings(fbid=commercemerchantsettings_id).get_setup_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_shipping_profiles(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceMerchantSettings(fbid=commercemerchantsettings_id).get_shipping_profiles(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_shops(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceMerchantSettings(fbid=commercemerchantsettings_id).get_shops(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_tax_settings(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = CommerceMerchantSettings(fbid=commercemerchantsettings_id).get_tax_settings(
        fields=fields,
        params=params,
    )

    return result


# Export the server
commercemerchantsettings_server = mcp
