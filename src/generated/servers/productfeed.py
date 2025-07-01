"""ProductFeed MCP Server with typed wrappers."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.productfeed import ProductFeed
from fastmcp import FastMCP

from src.generated.models.automotivemodel import AutomotiveModelField
from src.generated.models.destination import DestinationField
from src.generated.models.flight import FlightField
from src.generated.models.homelisting import HomeListingField
from src.generated.models.hotel import HotelField
from src.generated.models.mediatitle import MediaTitleField
from src.generated.models.productfeed import (
    ProductFeedCreateRuleParams,
    ProductFeedCreateSupplementaryFeedAssocParams,
    ProductFeedCreateUploadParams,
    ProductFeedCreateUploadScheduleParams,
    ProductFeedField,
    ProductFeedGetAutomotiveModelsParams,
    ProductFeedGetDestinationsParams,
    ProductFeedGetFlightsParams,
    ProductFeedGetHomeListingsParams,
    ProductFeedGetHotelsParams,
    ProductFeedGetMediaTitlesParams,
    ProductFeedGetProductsParams,
    ProductFeedGetVehicleOffersParams,
    ProductFeedGetVehiclesParams,
    ProductFeedUpdateParams,
)
from src.generated.models.productitem import ProductItemField
from src.generated.models.vehicle import VehicleField
from src.generated.models.vehicleoffer import VehicleOfferField
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


productfeed_server.tool(get_productfeed)


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


productfeed_server.tool(update_productfeed)


@wrapped_fn_tool
def delete_productfeed(
    productfeed_id: str,
) -> str:
    """Delete a ProductFeed object.

    Args:
        productfeed_id: The ID of the ProductFeed.
    """
    return ProductFeed(productfeed_id).api_delete()


productfeed_server.tool(delete_productfeed)


# ---- Edge Methods (13) ----
@wrapped_fn_tool
def get_automotive_models(
    productfeed_id: str,
    fields: list[AutomotiveModelField] = [],
    params: ProductFeedGetAutomotiveModelsParams = {},
) -> Any:
    """Get Automotive Models for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductFeed(productfeed_id).get_automotive_models(fields=fields, params=params)


productfeed_server.tool(get_automotive_models)


@wrapped_fn_tool
def get_destinations(
    productfeed_id: str,
    fields: list[DestinationField] = [],
    params: ProductFeedGetDestinationsParams = {},
) -> Any:
    """Get Destinations for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductFeed(productfeed_id).get_destinations(fields=fields, params=params)


productfeed_server.tool(get_destinations)


@wrapped_fn_tool
def get_flights(
    productfeed_id: str,
    fields: list[FlightField] = [],
    params: ProductFeedGetFlightsParams = {},
) -> Any:
    """Get Flights for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductFeed(productfeed_id).get_flights(fields=fields, params=params)


productfeed_server.tool(get_flights)


@wrapped_fn_tool
def get_home_listings(
    productfeed_id: str,
    fields: list[HomeListingField] = [],
    params: ProductFeedGetHomeListingsParams = {},
) -> Any:
    """Get Home Listings for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductFeed(productfeed_id).get_home_listings(fields=fields, params=params)


productfeed_server.tool(get_home_listings)


@wrapped_fn_tool
def get_hotels(
    productfeed_id: str,
    fields: list[HotelField] = [],
    params: ProductFeedGetHotelsParams = {},
) -> Any:
    """Get Hotels for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductFeed(productfeed_id).get_hotels(fields=fields, params=params)


productfeed_server.tool(get_hotels)


@wrapped_fn_tool
def get_media_titles(
    productfeed_id: str,
    fields: list[MediaTitleField] = [],
    params: ProductFeedGetMediaTitlesParams = {},
) -> Any:
    """Get Media Titles for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductFeed(productfeed_id).get_media_titles(fields=fields, params=params)


productfeed_server.tool(get_media_titles)


@wrapped_fn_tool
def get_products(
    productfeed_id: str,
    fields: list[ProductItemField] = [],
    params: ProductFeedGetProductsParams = {},
) -> Any:
    """Get Products for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductFeed(productfeed_id).get_products(fields=fields, params=params)


productfeed_server.tool(get_products)


@wrapped_fn_tool
def create_rule(
    productfeed_id: str,
    fields: list[str] = [],
    params: ProductFeedCreateRuleParams = {},
) -> Any:
    """Create Rule for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductFeed(productfeed_id).create_rule(fields=fields, params=params)


productfeed_server.tool(create_rule)


@wrapped_fn_tool
def create_supplementary_feed_assoc(
    productfeed_id: str,
    fields: list[str] = [],
    params: ProductFeedCreateSupplementaryFeedAssocParams = {},
) -> Any:
    """Create Supplementary Feed Assoc for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductFeed(productfeed_id).create_supplementary_feed_assoc(fields=fields, params=params)


productfeed_server.tool(create_supplementary_feed_assoc)


@wrapped_fn_tool
def create_upload_schedule(
    productfeed_id: str,
    fields: list[str] = [],
    params: ProductFeedCreateUploadScheduleParams = {},
) -> Any:
    """Create Upload Schedule for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductFeed(productfeed_id).create_upload_schedule(fields=fields, params=params)


productfeed_server.tool(create_upload_schedule)


@wrapped_fn_tool
def create_upload(
    productfeed_id: str,
    fields: list[str] = [],
    params: ProductFeedCreateUploadParams = {},
) -> Any:
    """Create Upload for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductFeed(productfeed_id).create_upload(fields=fields, params=params)


productfeed_server.tool(create_upload)


@wrapped_fn_tool
def get_vehicle_offers(
    productfeed_id: str,
    fields: list[VehicleOfferField] = [],
    params: ProductFeedGetVehicleOffersParams = {},
) -> Any:
    """Get Vehicle Offers for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductFeed(productfeed_id).get_vehicle_offers(fields=fields, params=params)


productfeed_server.tool(get_vehicle_offers)


@wrapped_fn_tool
def get_vehicles(
    productfeed_id: str,
    fields: list[VehicleField] = [],
    params: ProductFeedGetVehiclesParams = {},
) -> Any:
    """Get Vehicles for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductFeed(productfeed_id).get_vehicles(fields=fields, params=params)


productfeed_server.tool(get_vehicles)
