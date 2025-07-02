"""ProductCatalog MCP Server."""

from typing import Any

from facebook_business.adobjects.productcatalog import ProductCatalog
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookProductCatalog"
instructions = """
ProductCatalog MCP Server for Facebook Business API.

Provides typed access to all ProductCatalog operations.
"""

productcatalog_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@productcatalog_server.tool
@wrapped_fn_tool
def get_productcatalog(
    productcatalog_id: str,
    fields: list[str] = [],
) -> str:
    obj = ProductCatalog(productcatalog_id)
    return obj.api_get(fields=fields)


@productcatalog_server.tool
@wrapped_fn_tool
def update_productcatalog(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return ProductCatalog(productcatalog_id).api_update(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def delete_productcatalog(
    productcatalog_id: str,
) -> str:
    return ProductCatalog(productcatalog_id).api_delete()


# ---- Edge Methods (53) ----
@productcatalog_server.tool
@wrapped_fn_tool
def delete_agencies(
    productcatalog_id: str,
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).delete_agencies(params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_agencies(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_agencies(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_agencie(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_agencie(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def delete_assigned_users(
    productcatalog_id: str,
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).delete_assigned_users(params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_assigned_users(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_assigned_users(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_assigned_user(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_assigned_user(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_automotive_models(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_automotive_models(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_batch(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_catalog_store(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_catalog_store(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_categories(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_categories(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_categorie(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_categorie(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_check_batch_request_status(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_check_batch_request_status(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def get_check_marketplace_partner_sellers_status(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_check_marketplace_partner_sellers_status(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def get_collaborative_ads_lsb_image_bank(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_collaborative_ads_lsb_image_bank(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def get_collaborative_ads_share_settings(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_collaborative_ads_share_settings(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def create_cpas_lsb_image_bank(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_cpas_lsb_image_bank(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def get_creator_asset_creatives(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_creator_asset_creatives(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def get_data_sources(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_data_sources(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_destinations(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_destinations(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_diagnostics(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_diagnostics(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_event_stats(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_event_stats(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def delete_external_event_sources(
    productcatalog_id: str,
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).delete_external_event_sources(params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_external_event_sources(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_external_event_sources(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def create_external_event_source(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_external_event_source(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def get_flights(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_flights(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_geolocated_items_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_geolocated_items_batch(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def get_home_listings(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_home_listings(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_home_listing(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_home_listing(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_hotel_rooms_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_hotel_rooms_batch(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_hotel_rooms_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_hotel_rooms_batch(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_hotels(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_hotels(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_hotel(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_hotel(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_items_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_items_batch(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_localized_items_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_localized_items_batch(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def create_marketplace_partner_sellers_detail(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_marketplace_partner_sellers_detail(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def create_marketplace_partner_signal(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_marketplace_partner_signal(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def get_pricing_variables_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_pricing_variables_batch(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def create_pricing_variables_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_pricing_variables_batch(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def get_product_feeds(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_product_feeds(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_product_feed(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_product_feed(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_product_groups(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_product_groups(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_product_group(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_product_group(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_product_sets(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_product_sets(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_product_set(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_product_set(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_product_sets_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_product_sets_batch(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_products(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_products(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_product(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_product(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_update_generated_image_config(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_update_generated_image_config(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def get_vehicle_offers(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_vehicle_offers(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_vehicles(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_vehicles(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_vehicle(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_vehicle(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_version_configs(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).get_version_configs(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_version_items_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ProductCatalog(productcatalog_id).create_version_items_batch(
        fields=fields, params=params
    )
