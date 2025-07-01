"""Streamlined ProductCatalog MCP Server - Core Operations Only."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.productcatalog import ProductCatalog
from fastmcp import FastMCP

from src.generated.models.productcatalog import ProductCatalogField, ProductCatalogUpdateParams
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
@wrapped_fn_tool
def get_productcatalog(
    productcatalog_id: str,
    fields: list[ProductCatalogField] = [],
) -> str:
    """Get a ProductCatalog object by ID.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
    """
    obj = ProductCatalog(productcatalog_id)
    return obj.api_get(fields=fields)


@wrapped_fn_tool
def update_productcatalog(
    productcatalog_id: str,
    fields: list[ProductCatalogField] = [],
    params: ProductCatalogUpdateParams | dict[str, Any] = {},
) -> str:
    """Update a ProductCatalog object.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to return after update.
        params: Parameters to update.
    """
    return ProductCatalog(productcatalog_id).api_update(fields=fields, params=params)


@wrapped_fn_tool
def delete_productcatalog(
    productcatalog_id: str,
) -> str:
    """Delete a ProductCatalog object.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
    """
    return ProductCatalog(productcatalog_id).api_delete()


# ---- Edge Methods (46) ----
# Import and register wrapper functions from generated wrappers
from src.generated.wrappers.productcatalog_wrappers import (
    create_agency,
    create_assigned_user,
    create_batch,
    create_catalog_store,
    create_category,
    create_cpas_lsb_image_bank,
    create_external_event_source,
    create_geolocated_items_batch,
    create_home_listing,
    create_hotel,
    create_hotel_rooms_batch,
    create_items_batch,
    create_localized_items_batch,
    create_market_place_partner_sellers_detail,
    create_market_place_partner_signal,
    create_pricing_variables_batch,
    create_product,
    create_product_feed,
    create_product_group,
    create_product_set,
    create_update_generated_image_config,
    create_vehicle,
    create_version_items_batch,
    delete_agencies,
    delete_assigned_users,
    delete_external_event_sources,
    get_assigned_users,
    get_automotive_models,
    get_categories,
    get_check_batch_request_status,
    get_check_marketplace_partner_sellers_status,
    get_creator_asset_creatives,
    get_data_sources,
    get_destinations,
    get_diagnostics,
    get_event_stats,
    get_flights,
    get_home_listings,
    get_hotel_rooms_batch,
    get_hotels,
    get_pricing_variables_batch,
    get_product_sets,
    get_product_sets_batch,
    get_products,
    get_vehicle_offers,
    get_vehicles,
)

# ---- Register tools ----
# Register CRUD operations
productcatalog_server.tool(get_productcatalog)
productcatalog_server.tool(update_productcatalog)
productcatalog_server.tool(delete_productcatalog)

# Register edge methods from wrappers
productcatalog_server.tool(delete_agencies)
productcatalog_server.tool(create_agency)
productcatalog_server.tool(delete_assigned_users)
productcatalog_server.tool(get_assigned_users)
productcatalog_server.tool(create_assigned_user)
productcatalog_server.tool(get_automotive_models)
productcatalog_server.tool(create_batch)
productcatalog_server.tool(create_catalog_store)
productcatalog_server.tool(get_categories)
productcatalog_server.tool(create_category)
productcatalog_server.tool(get_check_batch_request_status)
productcatalog_server.tool(get_check_marketplace_partner_sellers_status)
productcatalog_server.tool(create_cpas_lsb_image_bank)
productcatalog_server.tool(get_creator_asset_creatives)
productcatalog_server.tool(get_data_sources)
productcatalog_server.tool(get_destinations)
productcatalog_server.tool(get_diagnostics)
productcatalog_server.tool(get_event_stats)
productcatalog_server.tool(delete_external_event_sources)
productcatalog_server.tool(create_external_event_source)
productcatalog_server.tool(get_flights)
productcatalog_server.tool(create_geolocated_items_batch)
productcatalog_server.tool(get_home_listings)
productcatalog_server.tool(create_home_listing)
productcatalog_server.tool(get_hotel_rooms_batch)
productcatalog_server.tool(create_hotel_rooms_batch)
productcatalog_server.tool(get_hotels)
productcatalog_server.tool(create_hotel)
productcatalog_server.tool(create_items_batch)
productcatalog_server.tool(create_localized_items_batch)
productcatalog_server.tool(create_market_place_partner_sellers_detail)
productcatalog_server.tool(create_market_place_partner_signal)
productcatalog_server.tool(get_pricing_variables_batch)
productcatalog_server.tool(create_pricing_variables_batch)
productcatalog_server.tool(create_product_feed)
productcatalog_server.tool(create_product_group)
productcatalog_server.tool(get_product_sets)
productcatalog_server.tool(create_product_set)
productcatalog_server.tool(get_product_sets_batch)
productcatalog_server.tool(get_products)
productcatalog_server.tool(create_product)
productcatalog_server.tool(create_update_generated_image_config)
productcatalog_server.tool(get_vehicle_offers)
productcatalog_server.tool(get_vehicles)
productcatalog_server.tool(create_vehicle)
productcatalog_server.tool(create_version_items_batch)
