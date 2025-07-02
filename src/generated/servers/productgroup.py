"""ProductGroup MCP Server."""

from typing import Any

from facebook_business.adobjects.productgroup import ProductGroup
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductGroup"
instructions = """
ProductGroup MCP Server for Facebook Business API.

Provides typed access to all ProductGroup operations.
"""

productgroup_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@productgroup_server.tool
@wrapped_fn_tool
def get_productgroup(
    productgroup_id: str,
    fields: list[str] = [],
) -> str:
    obj = ProductGroup(productgroup_id)
    return obj.api_get(fields=fields)


@productgroup_server.tool
@wrapped_fn_tool
def update_productgroup(
    productgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return ProductGroup(productgroup_id).api_update(fields=fields, params=params)


@productgroup_server.tool
@wrapped_fn_tool
def delete_productgroup(
    productgroup_id: str,
) -> str:
    return ProductGroup(productgroup_id).api_delete()


# ---- Edge Methods (2) ----
@productgroup_server.tool
@wrapped_fn_tool
def get_products(
    productgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductGroup(productgroup_id).get_products(fields=fields, params=params)


@productgroup_server.tool
@wrapped_fn_tool
def create_product(
    productgroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductGroup(productgroup_id).create_product(fields=fields, params=params)
