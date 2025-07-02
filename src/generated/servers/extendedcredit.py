"""ExtendedCredit MCP Server."""

from typing import Any

from facebook_business.adobjects.extendedcredit import ExtendedCredit
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = ExtendedCredit(extendedcredit_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (7) ----
@extendedcredit_server.tool
@wrapped_fn_tool
def get_extended_credit_invoice_groups(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ExtendedCredit(extendedcredit_id).get_extended_credit_invoice_groups(
        fields=fields, params=params
    )


@extendedcredit_server.tool
@wrapped_fn_tool
def create_extended_credit_invoice_group(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ExtendedCredit(extendedcredit_id).create_extended_credit_invoice_group(
        fields=fields, params=params
    )


@extendedcredit_server.tool
@wrapped_fn_tool
def get_owning_credit_allocation_configs(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ExtendedCredit(extendedcredit_id).get_owning_credit_allocation_configs(
        fields=fields, params=params
    )


@extendedcredit_server.tool
@wrapped_fn_tool
def create_owning_credit_allocation_config(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ExtendedCredit(extendedcredit_id).create_owning_credit_allocation_config(
        fields=fields, params=params
    )


@extendedcredit_server.tool
@wrapped_fn_tool
def create_whatsapp_credit_attach(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ExtendedCredit(extendedcredit_id).create_whatsapp_credit_attach(
        fields=fields, params=params
    )


@extendedcredit_server.tool
@wrapped_fn_tool
def create_whatsapp_credit_sharing(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ExtendedCredit(extendedcredit_id).create_whatsapp_credit_sharing(
        fields=fields, params=params
    )


@extendedcredit_server.tool
@wrapped_fn_tool
def create_whatsapp_credit_sharing_and_attach(
    extendedcredit_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ExtendedCredit(extendedcredit_id).create_whatsapp_credit_sharing_and_attach(
        fields=fields, params=params
    )
