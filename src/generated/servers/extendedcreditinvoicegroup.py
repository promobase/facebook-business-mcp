"""ExtendedCreditInvoiceGroup MCP Server with typed wrappers."""

from facebook_business.adobjects.extendedcreditinvoicegroup import ExtendedCreditInvoiceGroup
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.adaccount import AdAccountField
from src.generated.models.extendedcreditinvoicegroup import (
    ExtendedCreditInvoiceGroupCreateAdAccountParams,
    ExtendedCreditInvoiceGroupDeleteAdAccountsParams,
    ExtendedCreditInvoiceGroupField,
    ExtendedCreditInvoiceGroupUpdateParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookExtendedCreditInvoiceGroup"
instructions = """
ExtendedCreditInvoiceGroup MCP Server for Facebook Business API.

Provides typed access to all ExtendedCreditInvoiceGroup operations.
"""

extendedcreditinvoicegroup_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@extendedcreditinvoicegroup_server.tool
@wrapped_fn_tool
def get_extendedcreditinvoicegroup(
    extendedcreditinvoicegroup_id: str,
    fields: list[ExtendedCreditInvoiceGroupField] = [],
) -> str:
    """Get a ExtendedCreditInvoiceGroup object by ID.

    Args:
        extendedcreditinvoicegroup_id: The ID of the ExtendedCreditInvoiceGroup.
        fields: Fields to retrieve. Available fields: See ExtendedCreditInvoiceGroupField type.
    """
    obj = ExtendedCreditInvoiceGroup(extendedcreditinvoicegroup_id)
    return obj.api_get(fields=fields)


@extendedcreditinvoicegroup_server.tool
@wrapped_fn_tool
def update_extendedcreditinvoicegroup(
    extendedcreditinvoicegroup_id: str,
    fields: list[ExtendedCreditInvoiceGroupField] = [],
    params: ExtendedCreditInvoiceGroupUpdateParams | dict = {},
) -> str:
    """Update a ExtendedCreditInvoiceGroup object.

    Args:
        extendedcreditinvoicegroup_id: The ID of the ExtendedCreditInvoiceGroup.
        fields: Fields to return after update. Available fields: See ExtendedCreditInvoiceGroupField type.
        params: Parameters to update. Available params: See ExtendedCreditInvoiceGroupUpdateParams type.
    """
    return ExtendedCreditInvoiceGroup(extendedcreditinvoicegroup_id).api_update(
        fields=fields, params=params
    )


@extendedcreditinvoicegroup_server.tool
@wrapped_fn_tool
def delete_extendedcreditinvoicegroup(
    extendedcreditinvoicegroup_id: str,
) -> str:
    """Delete a ExtendedCreditInvoiceGroup object.

    Args:
        extendedcreditinvoicegroup_id: The ID of the ExtendedCreditInvoiceGroup.
    """
    return ExtendedCreditInvoiceGroup(extendedcreditinvoicegroup_id).api_delete()


# ---- Edge Methods (2) ----
@extendedcreditinvoicegroup_server.tool
@wrapped_fn_tool
def delete_ad_accounts(
    extendedcreditinvoicegroup_id: str,
    params: ExtendedCreditInvoiceGroupDeleteAdAccountsParams | dict = {},
):
    """Delete Ad Accounts for this ExtendedCreditInvoiceGroup.

    Args:
        extendedcreditinvoicegroup_id: The ID of the ExtendedCreditInvoiceGroup.
        params: Query parameters. Available params: See ExtendedCreditInvoiceGroupDeleteAdAccountsParams type.
    """
    return ExtendedCreditInvoiceGroup(extendedcreditinvoicegroup_id).delete_ad_accounts(
        params=params
    )


@extendedcreditinvoicegroup_server.tool
@wrapped_fn_tool
def create_ad_account(
    extendedcreditinvoicegroup_id: str,
    fields: list[str] = [],
    params: ExtendedCreditInvoiceGroupCreateAdAccountParams | dict = {},
):
    """Create Ad Account for this ExtendedCreditInvoiceGroup.

    Args:
        extendedcreditinvoicegroup_id: The ID of the ExtendedCreditInvoiceGroup.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ExtendedCreditInvoiceGroupCreateAdAccountParams type.
    """
    return ExtendedCreditInvoiceGroup(extendedcreditinvoicegroup_id).create_ad_account(
        fields=fields, params=params
    )
