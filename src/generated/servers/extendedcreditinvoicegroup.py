"""ExtendedCreditInvoiceGroup MCP Server."""

from typing import Any

from facebook_business.adobjects.extendedcreditinvoicegroup import ExtendedCreditInvoiceGroup
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = ExtendedCreditInvoiceGroup(extendedcreditinvoicegroup_id)
    return obj.api_get(fields=fields)


@extendedcreditinvoicegroup_server.tool
@wrapped_fn_tool
def update_extendedcreditinvoicegroup(
    extendedcreditinvoicegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return ExtendedCreditInvoiceGroup(extendedcreditinvoicegroup_id).api_update(
        fields=fields, params=params
    )


@extendedcreditinvoicegroup_server.tool
@wrapped_fn_tool
def delete_extendedcreditinvoicegroup(
    extendedcreditinvoicegroup_id: str,
) -> str:
    return ExtendedCreditInvoiceGroup(extendedcreditinvoicegroup_id).api_delete()


# ---- Edge Methods (2) ----
@extendedcreditinvoicegroup_server.tool
@wrapped_fn_tool
def delete_ad_accounts(
    extendedcreditinvoicegroup_id: str,
    params: dict[str, Any] = {},
):
    return ExtendedCreditInvoiceGroup(extendedcreditinvoicegroup_id).delete_ad_accounts(
        params=params
    )


@extendedcreditinvoicegroup_server.tool
@wrapped_fn_tool
def create_ad_account(
    extendedcreditinvoicegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ExtendedCreditInvoiceGroup(extendedcreditinvoicegroup_id).create_ad_account(
        fields=fields, params=params
    )
