"""ProductSet MCP Server with typed wrappers."""

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
@productset_server.tool
@wrapped_fn_tool
def get_productset(
    productset_id: str,
    fields: list[ProductSetField] = [],
) -> str:
    """Get a ProductSet object by ID.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve. Available fields: See ProductSetField type.
    """
    obj = ProductSet(productset_id)
    return obj.api_get(fields=fields)


@productset_server.tool
@wrapped_fn_tool
def update_productset(
    productset_id: str,
    fields: list[ProductSetField] = [],
    params: ProductSetUpdateParams | dict = {},
) -> str:
    """Update a ProductSet object.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to return after update. Available fields: See ProductSetField type.
        params: Parameters to update. Available params: See ProductSetUpdateParams type.
    """
    return ProductSet(productset_id).api_update(fields=fields, params=params)


@productset_server.tool
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
@productset_server.tool
@wrapped_fn_tool
def get_automotive_models(
    productset_id: str,
    fields: list[AutomotiveModelField] = [],
    params: ProductSetGetAutomotiveModelsParams | dict = {},
):
    """Get Automotive Models for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve. Available fields: See AutomotiveModelField type.
        params: Query parameters. Available params: See ProductSetGetAutomotiveModelsParams type.
    """
    return ProductSet(productset_id).get_automotive_models(fields=fields, params=params)


@productset_server.tool
@wrapped_fn_tool
def get_destinations(
    productset_id: str,
    fields: list[DestinationField] = [],
    params: ProductSetGetDestinationsParams | dict = {},
):
    """Get Destinations for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve. Available fields: See DestinationField type.
        params: Query parameters. Available params: See ProductSetGetDestinationsParams type.
    """
    return ProductSet(productset_id).get_destinations(fields=fields, params=params)


@productset_server.tool
@wrapped_fn_tool
def get_flights(
    productset_id: str,
    fields: list[FlightField] = [],
    params: ProductSetGetFlightsParams | dict = {},
):
    """Get Flights for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve. Available fields: See FlightField type.
        params: Query parameters. Available params: See ProductSetGetFlightsParams type.
    """
    return ProductSet(productset_id).get_flights(fields=fields, params=params)


@productset_server.tool
@wrapped_fn_tool
def get_home_listings(
    productset_id: str,
    fields: list[HomeListingField] = [],
    params: ProductSetGetHomeListingsParams | dict = {},
):
    """Get Home Listings for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve. Available fields: See HomeListingField type.
        params: Query parameters. Available params: See ProductSetGetHomeListingsParams type.
    """
    return ProductSet(productset_id).get_home_listings(fields=fields, params=params)


@productset_server.tool
@wrapped_fn_tool
def get_hotels(
    productset_id: str,
    fields: list[HotelField] = [],
    params: ProductSetGetHotelsParams | dict = {},
):
    """Get Hotels for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve. Available fields: See HotelField type.
        params: Query parameters. Available params: See ProductSetGetHotelsParams type.
    """
    return ProductSet(productset_id).get_hotels(fields=fields, params=params)


@productset_server.tool
@wrapped_fn_tool
def get_media_titles(
    productset_id: str,
    fields: list[MediaTitleField] = [],
    params: ProductSetGetMediaTitlesParams | dict = {},
):
    """Get Media Titles for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve. Available fields: See MediaTitleField type.
        params: Query parameters. Available params: See ProductSetGetMediaTitlesParams type.
    """
    return ProductSet(productset_id).get_media_titles(fields=fields, params=params)


@productset_server.tool
@wrapped_fn_tool
def get_products(
    productset_id: str,
    fields: list[ProductItemField] = [],
    params: ProductSetGetProductsParams | dict = {},
):
    """Get Products for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve. Available fields: See ProductItemField type.
        params: Query parameters. Available params: See ProductSetGetProductsParams type.
    """
    return ProductSet(productset_id).get_products(fields=fields, params=params)


@productset_server.tool
@wrapped_fn_tool
def get_vehicle_offers(
    productset_id: str,
    fields: list[VehicleOfferField] = [],
    params: ProductSetGetVehicleOffersParams | dict = {},
):
    """Get Vehicle Offers for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve. Available fields: See VehicleOfferField type.
        params: Query parameters. Available params: See ProductSetGetVehicleOffersParams type.
    """
    return ProductSet(productset_id).get_vehicle_offers(fields=fields, params=params)


@productset_server.tool
@wrapped_fn_tool
def get_vehicles(
    productset_id: str,
    fields: list[VehicleField] = [],
    params: ProductSetGetVehiclesParams | dict = {},
):
    """Get Vehicles for this ProductSet.

    Args:
        productset_id: The ID of the ProductSet.
        fields: Fields to retrieve. Available fields: See VehicleField type.
        params: Query parameters. Available params: See ProductSetGetVehiclesParams type.
    """
    return ProductSet(productset_id).get_vehicles(fields=fields, params=params)
