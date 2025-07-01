"""Streamlined ProductSet MCP Server - Core Operations Only."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.productset import ProductSet
from fastmcp import FastMCP

from src.generated.models.productset import ProductSetField, ProductSetUpdateParams
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
@wrapped_fn_tool
def get_productset(
    productset_id: str,
    fields: list[ProductSetField] = [],
) -> str:
    """Get a ProductSet object by ID.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve.
    """
    obj = ProductSet(productset_id)
    return obj.api_get(fields=fields)


@wrapped_fn_tool
def update_productset(
    productset_id: str,
    fields: list[ProductSetField] = [],
    params: ProductSetUpdateParams | dict[str, Any] = {},
) -> str:
    """Update a ProductSet object.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to return after update.
        params: Parameters to update.
    """
    return ProductSet(productset_id).api_update(fields=fields, params=params)


@wrapped_fn_tool
def delete_productset(
    productset_id: str,
) -> str:
    """Delete a ProductSet object.

    Args:
        productset_id: The ID of the ProductSet.
    """
    return ProductSet(productset_id).api_delete()


# ---- Edge Methods (9) ----
# Import and register wrapper functions from generated wrappers
from src.generated.wrappers.productset_wrappers import (
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
productset_server.tool(get_productset)
productset_server.tool(update_productset)
productset_server.tool(delete_productset)

# Register edge methods from wrappers
productset_server.tool(get_automotive_models)
productset_server.tool(get_destinations)
productset_server.tool(get_flights)
productset_server.tool(get_home_listings)
productset_server.tool(get_hotels)
productset_server.tool(get_media_titles)
productset_server.tool(get_products)
productset_server.tool(get_vehicle_offers)
productset_server.tool(get_vehicles)
