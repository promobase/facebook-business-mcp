"""CommerceOrder MCP Server."""

from typing import Any

from facebook_business.adobjects.commerceorder import CommerceOrder
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCommerceOrder"
instructions = """
CommerceOrder MCP Server for Facebook Business API.

Provides typed access to all CommerceOrder operations.
"""

commerceorder_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@commerceorder_server.tool
@wrapped_fn_tool
def get_commerceorder(
    commerceorder_id: str,
    fields: list[str] = [],
) -> str:
    obj = CommerceOrder(commerceorder_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (8) ----
@commerceorder_server.tool
@wrapped_fn_tool
def create_acknowledge_order(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceOrder(commerceorder_id).create_acknowledge_order(fields=fields, params=params)


@commerceorder_server.tool
@wrapped_fn_tool
def create_cancellation(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceOrder(commerceorder_id).create_cancellation(fields=fields, params=params)


@commerceorder_server.tool
@wrapped_fn_tool
def create_item_update(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceOrder(commerceorder_id).create_item_update(fields=fields, params=params)


@commerceorder_server.tool
@wrapped_fn_tool
def create_refund(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceOrder(commerceorder_id).create_refund(fields=fields, params=params)


@commerceorder_server.tool
@wrapped_fn_tool
def get_returns(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceOrder(commerceorder_id).get_returns(fields=fields, params=params)


@commerceorder_server.tool
@wrapped_fn_tool
def create_return(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceOrder(commerceorder_id).create_return(fields=fields, params=params)


@commerceorder_server.tool
@wrapped_fn_tool
def create_shipment(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceOrder(commerceorder_id).create_shipment(fields=fields, params=params)


@commerceorder_server.tool
@wrapped_fn_tool
def create_update_shipment(
    commerceorder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CommerceOrder(commerceorder_id).create_update_shipment(fields=fields, params=params)
