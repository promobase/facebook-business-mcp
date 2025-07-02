"""CommerceOrderTransactionDetail MCP Server."""

from typing import Any

from facebook_business.adobjects.commerceordertransactiondetail import (
    CommerceOrderTransactionDetail,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCommerceOrderTransactionDetail"
instructions = """
CommerceOrderTransactionDetail MCP Server for Facebook Business API.

Provides typed access to all CommerceOrderTransactionDetail operations.
"""

commerceordertransactiondetail_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (2) ----
@commerceordertransactiondetail_server.tool
@wrapped_fn_tool
def get_items(
    commerceordertransactiondetail_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceOrderTransactionDetail(commerceordertransactiondetail_id).get_items(
        fields=fields, params=params
    )


@commerceordertransactiondetail_server.tool
@wrapped_fn_tool
def get_tax_details(
    commerceordertransactiondetail_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceOrderTransactionDetail(commerceordertransactiondetail_id).get_tax_details(
        fields=fields, params=params
    )
