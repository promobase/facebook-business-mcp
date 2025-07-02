"""ProductItem MCP Server."""

from typing import Any

from facebook_business.adobjects.productitem import ProductItem
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductItem"
instructions = """
ProductItem MCP Server for Facebook Business API.

Provides typed access to all ProductItem operations.
"""

productitem_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@productitem_server.tool
@wrapped_fn_tool
def get_productitem(
    productitem_id: str,
    fields: list[str] = [],
) -> str:
    obj = ProductItem(productitem_id)
    return obj.api_get(fields=fields)


@productitem_server.tool
@wrapped_fn_tool
def update_productitem(
    productitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return ProductItem(productitem_id).api_update(fields=fields, params=params)


@productitem_server.tool
@wrapped_fn_tool
def delete_productitem(
    productitem_id: str,
) -> str:
    return ProductItem(productitem_id).api_delete()


# ---- Edge Methods (4) ----
@productitem_server.tool
@wrapped_fn_tool
def get_channels_to_integrity_status(
    productitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductItem(productitem_id).get_channels_to_integrity_status(
        fields=fields, params=params
    )


@productitem_server.tool
@wrapped_fn_tool
def get_override_details(
    productitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductItem(productitem_id).get_override_details(fields=fields, params=params)


@productitem_server.tool
@wrapped_fn_tool
def get_product_sets(
    productitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductItem(productitem_id).get_product_sets(fields=fields, params=params)


@productitem_server.tool
@wrapped_fn_tool
def get_videos_metadata(
    productitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductItem(productitem_id).get_videos_metadata(fields=fields, params=params)
