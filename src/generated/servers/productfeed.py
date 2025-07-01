"""Streamlined ProductFeed MCP Server - Core Operations Only."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.productfeed import ProductFeed
from fastmcp import FastMCP

from src.generated.models.productfeed import ProductFeedField, ProductFeedUpdateParams
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
@wrapped_fn_tool
def get_productfeed(
    productfeed_id: str,
    fields: list[ProductFeedField] = [],
) -> str:
    """Get a ProductFeed object by ID.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
    """
    obj = ProductFeed(productfeed_id)
    return obj.api_get(fields=fields)


@wrapped_fn_tool
def update_productfeed(
    productfeed_id: str,
    fields: list[ProductFeedField] = [],
    params: ProductFeedUpdateParams | dict[str, Any] = {},
) -> str:
    """Update a ProductFeed object.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to return after update.
        params: Parameters to update.
    """
    return ProductFeed(productfeed_id).api_update(fields=fields, params=params)


@wrapped_fn_tool
def delete_productfeed(
    productfeed_id: str,
) -> str:
    """Delete a ProductFeed object.

    Args:
        productfeed_id: The ID of the ProductFeed.
    """
    return ProductFeed(productfeed_id).api_delete()


# ---- Edge Methods (13) ----
# Import and register wrapper functions from generated wrappers
from src.generated.wrappers.productfeed_wrappers import (
    create_rule,
    create_supplementary_feed_assoc,
    create_upload,
    create_upload_schedule,
    get_automotive_models,
    get_destinations,
    get_flights,
    get_home_listings,
    get_hotels,
    get_media_titles,
    get_products,
    get_vehicle_offers,
    get_vehicles,
)

# ---- Register tools ----
# Register CRUD operations
productfeed_server.tool(get_productfeed)
productfeed_server.tool(update_productfeed)
productfeed_server.tool(delete_productfeed)

# Register edge methods from wrappers
productfeed_server.tool(get_automotive_models)
productfeed_server.tool(get_destinations)
productfeed_server.tool(get_flights)
productfeed_server.tool(get_home_listings)
productfeed_server.tool(get_hotels)
productfeed_server.tool(get_media_titles)
productfeed_server.tool(get_products)
productfeed_server.tool(create_rule)
productfeed_server.tool(create_supplementary_feed_assoc)
productfeed_server.tool(create_upload_schedule)
productfeed_server.tool(create_upload)
productfeed_server.tool(get_vehicle_offers)
productfeed_server.tool(get_vehicles)
