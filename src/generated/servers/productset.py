"""ProductSet MCP Server."""

from typing import Any

from facebook_business.adobjects.productset import ProductSet
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductSet"
instructions = """
ProductSet MCP Server for Facebook Business API.

Provides typed access to all ProductSet operations.
"""

productset_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@productset_server.tool
@wrapped_fn_tool
def get_productset(
    productset_id: str,
    fields: list[str] = [],
) -> str:
    obj = ProductSet(productset_id)
    return obj.api_get(fields=fields)


@productset_server.tool
@wrapped_fn_tool
def update_productset(
    productset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return ProductSet(productset_id).api_update(fields=fields, params=params)


@productset_server.tool
@wrapped_fn_tool
def delete_productset(
    productset_id: str,
) -> str:
    return ProductSet(productset_id).api_delete()


# ---- Edge Methods (9) ----
@productset_server.tool
@wrapped_fn_tool
def get_automotive_models(
    productset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductSet(productset_id).get_automotive_models(fields=fields, params=params)


@productset_server.tool
@wrapped_fn_tool
def get_destinations(
    productset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductSet(productset_id).get_destinations(fields=fields, params=params)


@productset_server.tool
@wrapped_fn_tool
def get_flights(
    productset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductSet(productset_id).get_flights(fields=fields, params=params)


@productset_server.tool
@wrapped_fn_tool
def get_home_listings(
    productset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductSet(productset_id).get_home_listings(fields=fields, params=params)


@productset_server.tool
@wrapped_fn_tool
def get_hotels(
    productset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductSet(productset_id).get_hotels(fields=fields, params=params)


@productset_server.tool
@wrapped_fn_tool
def get_media_titles(
    productset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductSet(productset_id).get_media_titles(fields=fields, params=params)


@productset_server.tool
@wrapped_fn_tool
def get_products(
    productset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductSet(productset_id).get_products(fields=fields, params=params)


@productset_server.tool
@wrapped_fn_tool
def get_vehicle_offers(
    productset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductSet(productset_id).get_vehicle_offers(fields=fields, params=params)


@productset_server.tool
@wrapped_fn_tool
def get_vehicles(
    productset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductSet(productset_id).get_vehicles(fields=fields, params=params)
