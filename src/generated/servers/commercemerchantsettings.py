"""CommerceMerchantSettings MCP Server."""

from typing import Any

from facebook_business.adobjects.commercemerchantsettings import CommerceMerchantSettings
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCommerceMerchantSettings"
instructions = """
CommerceMerchantSettings MCP Server for Facebook Business API.

Provides typed access to all CommerceMerchantSettings operations.
"""

commercemerchantsettings_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@commercemerchantsettings_server.tool
@wrapped_fn_tool
def get_commercemerchantsettings(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
) -> str:
    obj = CommerceMerchantSettings(commercemerchantsettings_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (13) ----
@commercemerchantsettings_server.tool
@wrapped_fn_tool
def create_acknowledge_order(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceMerchantSettings(commercemerchantsettings_id).create_acknowledge_order(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def get_commerce_orders(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceMerchantSettings(commercemerchantsettings_id).get_commerce_orders(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def get_commerce_payouts(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceMerchantSettings(commercemerchantsettings_id).get_commerce_payouts(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def get_commerce_transactions(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceMerchantSettings(commercemerchantsettings_id).get_commerce_transactions(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def get_order_management_apps(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceMerchantSettings(commercemerchantsettings_id).get_order_management_apps(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def create_order_management_app(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceMerchantSettings(commercemerchantsettings_id).create_order_management_app(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def get_product_catalogs(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceMerchantSettings(commercemerchantsettings_id).get_product_catalogs(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def get_returns(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceMerchantSettings(commercemerchantsettings_id).get_returns(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def get_setup_status(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceMerchantSettings(commercemerchantsettings_id).get_setup_status(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def get_shipping_profiles(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceMerchantSettings(commercemerchantsettings_id).get_shipping_profiles(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def create_shipping_profile(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceMerchantSettings(commercemerchantsettings_id).create_shipping_profile(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def get_shops(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceMerchantSettings(commercemerchantsettings_id).get_shops(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def get_tax_settings(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceMerchantSettings(commercemerchantsettings_id).get_tax_settings(
        fields=fields, params=params
    )
