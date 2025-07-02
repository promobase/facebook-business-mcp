"""ExtendedCredit MCP Server with typed wrappers."""

from facebook_business.adobjects.extendedcredit import ExtendedCredit
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.extendedcredit import (
    ExtendedCreditCreateExtendedCreditInvoiceGroupParams,
    ExtendedCreditCreateOwningCreditAllocationConfigParams,
    ExtendedCreditCreateWhatsAppCreditAttachParams,
    ExtendedCreditCreateWhatsAppCreditSharingAndAttachParams,
    ExtendedCreditCreateWhatsAppCreditSharingParams,
    ExtendedCreditField,
    ExtendedCreditGetOwningCreditAllocationConfigsParams,
)
from src.generated.models.extendedcreditallocationconfig import ExtendedCreditAllocationConfigField
from src.generated.models.extendedcreditinvoicegroup import ExtendedCreditInvoiceGroupField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookExtendedCredit"
instructions = """
ExtendedCredit MCP Server for Facebook Business API.

Provides typed access to all ExtendedCredit operations.
"""

extendedcredit_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@extendedcredit_server.tool
@wrapped_fn_tool
def get_extendedcredit(
    extendedcredit_id: str,
    fields: list[ExtendedCreditField] = [],
) -> str:
    """Get a ExtendedCredit object by ID.

    Args:
        extendedcredit_id: The ID of the ExtendedCredit.
        fields: Fields to retrieve. Available fields: See ExtendedCreditField type.
    """
    obj = ExtendedCredit(extendedcredit_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (6) ----
@extendedcredit_server.tool
@wrapped_fn_tool
def create_extended_credit_invoice_group(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: ExtendedCreditCreateExtendedCreditInvoiceGroupParams | dict = {},
):
    """Create Extended Credit Invoice Group for this ExtendedCredit.

    Args:
        extendedcredit_id: The ID of the ExtendedCredit.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ExtendedCreditCreateExtendedCreditInvoiceGroupParams type.
    """
    return ExtendedCredit(extendedcredit_id).create_extended_credit_invoice_group(
        fields=fields, params=params
    )


@extendedcredit_server.tool
@wrapped_fn_tool
def get_owning_credit_allocation_configs(
    extendedcredit_id: str,
    fields: list[ExtendedCreditAllocationConfigField] = [],
    params: ExtendedCreditGetOwningCreditAllocationConfigsParams | dict = {},
):
    """Get Owning Credit Allocation Configs for this ExtendedCredit.

    Args:
        extendedcredit_id: The ID of the ExtendedCredit.
        fields: Fields to retrieve. Available fields: See ExtendedCreditAllocationConfigField type.
        params: Query parameters. Available params: See ExtendedCreditGetOwningCreditAllocationConfigsParams type.
    """
    return ExtendedCredit(extendedcredit_id).get_owning_credit_allocation_configs(
        fields=fields, params=params
    )


@extendedcredit_server.tool
@wrapped_fn_tool
def create_owning_credit_allocation_config(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: ExtendedCreditCreateOwningCreditAllocationConfigParams | dict = {},
):
    """Create Owning Credit Allocation Config for this ExtendedCredit.

    Args:
        extendedcredit_id: The ID of the ExtendedCredit.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ExtendedCreditCreateOwningCreditAllocationConfigParams type.
    """
    return ExtendedCredit(extendedcredit_id).create_owning_credit_allocation_config(
        fields=fields, params=params
    )


@extendedcredit_server.tool
@wrapped_fn_tool
def create_whats_app_credit_attach(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: ExtendedCreditCreateWhatsAppCreditAttachParams | dict = {},
):
    """Create Whats App Credit Attach for this ExtendedCredit.

    Args:
        extendedcredit_id: The ID of the ExtendedCredit.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ExtendedCreditCreateWhatsAppCreditAttachParams type.
    """
    return ExtendedCredit(extendedcredit_id).create_whats_app_credit_attach(
        fields=fields, params=params
    )


@extendedcredit_server.tool
@wrapped_fn_tool
def create_whats_app_credit_sharing(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: ExtendedCreditCreateWhatsAppCreditSharingParams | dict = {},
):
    """Create Whats App Credit Sharing for this ExtendedCredit.

    Args:
        extendedcredit_id: The ID of the ExtendedCredit.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ExtendedCreditCreateWhatsAppCreditSharingParams type.
    """
    return ExtendedCredit(extendedcredit_id).create_whats_app_credit_sharing(
        fields=fields, params=params
    )


@extendedcredit_server.tool
@wrapped_fn_tool
def create_whats_app_credit_sharing_and_attach(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: ExtendedCreditCreateWhatsAppCreditSharingAndAttachParams | dict = {},
):
    """Create Whats App Credit Sharing And Attach for this ExtendedCredit.

    Args:
        extendedcredit_id: The ID of the ExtendedCredit.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ExtendedCreditCreateWhatsAppCreditSharingAndAttachParams type.
    """
    return ExtendedCredit(extendedcredit_id).create_whats_app_credit_sharing_and_attach(
        fields=fields, params=params
    )
