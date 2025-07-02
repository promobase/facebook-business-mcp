"""CommerceMerchantSettings MCP Server with typed wrappers."""

from facebook_business.adobjects.commercemerchantsettings import CommerceMerchantSettings
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.commercemerchantsettings import (
    CommerceMerchantSettingsCreateAcknowledgeOrderParams,
    CommerceMerchantSettingsCreateShippingProfileParams,
    CommerceMerchantSettingsField,
    CommerceMerchantSettingsGetCommerceOrdersParams,
    CommerceMerchantSettingsGetCommercePayoutsParams,
    CommerceMerchantSettingsGetCommerceTransactionsParams,
    CommerceMerchantSettingsGetReturnsParams,
    CommerceMerchantSettingsGetShippingProfilesParams,
)
from src.generated.models.commerceorder import CommerceOrderField
from src.generated.models.commerceordertransactiondetail import CommerceOrderTransactionDetailField
from src.generated.models.commercepayout import CommercePayoutField
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
    fields: list[CommerceMerchantSettingsField] = [],
) -> str:
    """Get a CommerceMerchantSettings object by ID.

    Args:
        commercemerchantsettings_id: The ID of the CommerceMerchantSettings.
        fields: Fields to retrieve. Available fields: See CommerceMerchantSettingsField type.
    """
    obj = CommerceMerchantSettings(commercemerchantsettings_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (7) ----
@commercemerchantsettings_server.tool
@wrapped_fn_tool
def create_acknowledge_order(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: CommerceMerchantSettingsCreateAcknowledgeOrderParams | dict = {},
):
    """Create Acknowledge Order for this CommerceMerchantSettings.

    Args:
        commercemerchantsettings_id: The ID of the CommerceMerchantSettings.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CommerceMerchantSettingsCreateAcknowledgeOrderParams type.
    """
    return CommerceMerchantSettings(commercemerchantsettings_id).create_acknowledge_order(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def get_commerce_orders(
    commercemerchantsettings_id: str,
    fields: list[CommerceOrderField] = [],
    params: CommerceMerchantSettingsGetCommerceOrdersParams | dict = {},
):
    """Get Commerce Orders for this CommerceMerchantSettings.

    Args:
        commercemerchantsettings_id: The ID of the CommerceMerchantSettings.
        fields: Fields to retrieve. Available fields: See CommerceOrderField type.
        params: Query parameters. Available params: See CommerceMerchantSettingsGetCommerceOrdersParams type.
    """
    return CommerceMerchantSettings(commercemerchantsettings_id).get_commerce_orders(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def get_commerce_payouts(
    commercemerchantsettings_id: str,
    fields: list[CommercePayoutField] = [],
    params: CommerceMerchantSettingsGetCommercePayoutsParams | dict = {},
):
    """Get Commerce Payouts for this CommerceMerchantSettings.

    Args:
        commercemerchantsettings_id: The ID of the CommerceMerchantSettings.
        fields: Fields to retrieve. Available fields: See CommercePayoutField type.
        params: Query parameters. Available params: See CommerceMerchantSettingsGetCommercePayoutsParams type.
    """
    return CommerceMerchantSettings(commercemerchantsettings_id).get_commerce_payouts(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def get_commerce_transactions(
    commercemerchantsettings_id: str,
    fields: list[CommerceOrderTransactionDetailField] = [],
    params: CommerceMerchantSettingsGetCommerceTransactionsParams | dict = {},
):
    """Get Commerce Transactions for this CommerceMerchantSettings.

    Args:
        commercemerchantsettings_id: The ID of the CommerceMerchantSettings.
        fields: Fields to retrieve. Available fields: See CommerceOrderTransactionDetailField type.
        params: Query parameters. Available params: See CommerceMerchantSettingsGetCommerceTransactionsParams type.
    """
    return CommerceMerchantSettings(commercemerchantsettings_id).get_commerce_transactions(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def get_returns(
    commercemerchantsettings_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: CommerceMerchantSettingsGetReturnsParams | dict = {},
):
    """Get Returns for this CommerceMerchantSettings.

    Args:
        commercemerchantsettings_id: The ID of the CommerceMerchantSettings.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See CommerceMerchantSettingsGetReturnsParams type.
    """
    return CommerceMerchantSettings(commercemerchantsettings_id).get_returns(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def get_shipping_profiles(
    commercemerchantsettings_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: CommerceMerchantSettingsGetShippingProfilesParams | dict = {},
):
    """Get Shipping Profiles for this CommerceMerchantSettings.

    Args:
        commercemerchantsettings_id: The ID of the CommerceMerchantSettings.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See CommerceMerchantSettingsGetShippingProfilesParams type.
    """
    return CommerceMerchantSettings(commercemerchantsettings_id).get_shipping_profiles(
        fields=fields, params=params
    )


@commercemerchantsettings_server.tool
@wrapped_fn_tool
def create_shipping_profile(
    commercemerchantsettings_id: str,
    fields: list[str] = [],
    params: CommerceMerchantSettingsCreateShippingProfileParams | dict = {},
):
    """Create Shipping Profile for this CommerceMerchantSettings.

    Args:
        commercemerchantsettings_id: The ID of the CommerceMerchantSettings.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CommerceMerchantSettingsCreateShippingProfileParams type.
    """
    return CommerceMerchantSettings(commercemerchantsettings_id).create_shipping_profile(
        fields=fields, params=params
    )
