"""ProductSet MCP Server with typed wrappers."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.productset import ProductSet
from fastmcp import FastMCP

from src.generated.models.automotivemodel import AutomotiveModelField
from src.generated.models.destination import DestinationField
from src.generated.models.flight import FlightField
from src.generated.models.homelisting import HomeListingField
from src.generated.models.hotel import HotelField
from src.generated.models.mediatitle import MediaTitleField
from src.generated.models.productitem import ProductItemField
from src.generated.models.productset import (
    ProductSetField,
    ProductSetGetAutomotiveModelsParams,
    ProductSetGetDestinationsParams,
    ProductSetGetFlightsParams,
    ProductSetGetHomeListingsParams,
    ProductSetGetHotelsParams,
    ProductSetGetMediaTitlesParams,
    ProductSetGetProductsParams,
    ProductSetGetVehicleOffersParams,
    ProductSetGetVehiclesParams,
    ProductSetUpdateParams,
)
from src.generated.models.vehicle import VehicleField
from src.generated.models.vehicleoffer import VehicleOfferField
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


productset_server.tool(get_productset)


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


productset_server.tool(update_productset)


@wrapped_fn_tool
def delete_productset(
    productset_id: str,
) -> str:
    """Delete a ProductSet object.

    Args:
        productset_id: The ID of the ProductSet.
    """
    return ProductSet(productset_id).api_delete()


productset_server.tool(delete_productset)


# ---- Edge Methods (9) ----
@wrapped_fn_tool
def get_automotive_models(
    productset_id: str,
    fields: list[AutomotiveModelField] = [],
    params: ProductSetGetAutomotiveModelsParams = {},
) -> Any:
    """Get Automotive Models for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductSet(productset_id).get_automotive_models(fields=fields, params=params)


productset_server.tool(get_automotive_models)


@wrapped_fn_tool
def get_destinations(
    productset_id: str,
    fields: list[DestinationField] = [],
    params: ProductSetGetDestinationsParams = {},
) -> Any:
    """Get Destinations for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductSet(productset_id).get_destinations(fields=fields, params=params)


productset_server.tool(get_destinations)


@wrapped_fn_tool
def get_flights(
    productset_id: str,
    fields: list[FlightField] = [],
    params: ProductSetGetFlightsParams = {},
) -> Any:
    """Get Flights for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductSet(productset_id).get_flights(fields=fields, params=params)


productset_server.tool(get_flights)


@wrapped_fn_tool
def get_home_listings(
    productset_id: str,
    fields: list[HomeListingField] = [],
    params: ProductSetGetHomeListingsParams = {},
) -> Any:
    """Get Home Listings for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductSet(productset_id).get_home_listings(fields=fields, params=params)


productset_server.tool(get_home_listings)


@wrapped_fn_tool
def get_hotels(
    productset_id: str,
    fields: list[HotelField] = [],
    params: ProductSetGetHotelsParams = {},
) -> Any:
    """Get Hotels for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductSet(productset_id).get_hotels(fields=fields, params=params)


productset_server.tool(get_hotels)


@wrapped_fn_tool
def get_media_titles(
    productset_id: str,
    fields: list[MediaTitleField] = [],
    params: ProductSetGetMediaTitlesParams = {},
) -> Any:
    """Get Media Titles for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductSet(productset_id).get_media_titles(fields=fields, params=params)


productset_server.tool(get_media_titles)


@wrapped_fn_tool
def get_products(
    productset_id: str,
    fields: list[ProductItemField] = [],
    params: ProductSetGetProductsParams = {},
) -> Any:
    """Get Products for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductSet(productset_id).get_products(fields=fields, params=params)


productset_server.tool(get_products)


@wrapped_fn_tool
def get_vehicle_offers(
    productset_id: str,
    fields: list[VehicleOfferField] = [],
    params: ProductSetGetVehicleOffersParams = {},
) -> Any:
    """Get Vehicle Offers for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductSet(productset_id).get_vehicle_offers(fields=fields, params=params)


productset_server.tool(get_vehicle_offers)


@wrapped_fn_tool
def get_vehicles(
    productset_id: str,
    fields: list[VehicleField] = [],
    params: ProductSetGetVehiclesParams = {},
) -> Any:
    """Get Vehicles for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductSet(productset_id).get_vehicles(fields=fields, params=params)


productset_server.tool(get_vehicles)
