"""ProductFeed MCP Server."""

from typing import Any

from facebook_business.adobjects.productfeed import ProductFeed
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductFeed"
instructions = """
ProductFeed MCP Server for Facebook Business API.

Provides typed access to all ProductFeed operations.
"""

productfeed_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@productfeed_server.tool
@wrapped_fn_tool
def get_productfeed(
    productfeed_id: str,
    fields: list[str] = [],
) -> str:
    obj = ProductFeed(productfeed_id)
    return obj.api_get(fields=fields)


@productfeed_server.tool
@wrapped_fn_tool
def update_productfeed(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return ProductFeed(productfeed_id).api_update(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def delete_productfeed(
    productfeed_id: str,
) -> str:
    return ProductFeed(productfeed_id).api_delete()


# ---- Edge Methods (13) ----
@productfeed_server.tool
@wrapped_fn_tool
def get_automotive_models(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductFeed(productfeed_id).get_automotive_models(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def get_destinations(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductFeed(productfeed_id).get_destinations(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def get_flights(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductFeed(productfeed_id).get_flights(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def get_home_listings(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductFeed(productfeed_id).get_home_listings(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def get_hotels(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductFeed(productfeed_id).get_hotels(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def get_media_titles(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductFeed(productfeed_id).get_media_titles(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def get_products(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductFeed(productfeed_id).get_products(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def create_rule(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductFeed(productfeed_id).create_rule(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def create_supplementary_feed_assoc(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductFeed(productfeed_id).create_supplementary_feed_assoc(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def create_upload_schedule(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductFeed(productfeed_id).create_upload_schedule(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def create_upload(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductFeed(productfeed_id).create_upload(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def get_vehicle_offers(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductFeed(productfeed_id).get_vehicle_offers(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def get_vehicles(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductFeed(productfeed_id).get_vehicles(fields=fields, params=params)
