"""ProductFeed MCP Server with typed wrappers."""

from __future__ import annotations

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
    """Get a ProductFeed object by ID.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve. Available fields: See {server_info.object_name}Field type.
    """
    obj = ProductFeed(productfeed_id)
    return obj.api_get(fields=fields)


@productfeed_server.tool
@wrapped_fn_tool
def update_productfeed(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict = {},
) -> str:
    """Update a ProductFeed object.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to return after update. Available fields: See {server_info.object_name}Field type.
        params: Parameters to update. Available params: See ProductFeedUpdateParams type.
    """
    return ProductFeed(productfeed_id).api_update(fields=fields, params=params)


@productfeed_server.tool
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
@productfeed_server.tool
@wrapped_fn_tool
def get_automotive_models(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Automotive Models for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve. Available fields: See AutomotiveModelField type.
        params: Query parameters. Available params: See ProductFeedGetAutomotiveModelsParams type.
    """
    return ProductFeed(productfeed_id).get_automotive_models(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def get_destinations(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Destinations for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve. Available fields: See DestinationField type.
        params: Query parameters. Available params: See ProductFeedGetDestinationsParams type.
    """
    return ProductFeed(productfeed_id).get_destinations(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def get_flights(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Flights for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve. Available fields: See FlightField type.
        params: Query parameters. Available params: See ProductFeedGetFlightsParams type.
    """
    return ProductFeed(productfeed_id).get_flights(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def get_home_listings(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Home Listings for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve. Available fields: See HomeListingField type.
        params: Query parameters. Available params: See ProductFeedGetHomeListingsParams type.
    """
    return ProductFeed(productfeed_id).get_home_listings(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def get_hotels(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Hotels for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve. Available fields: See HotelField type.
        params: Query parameters. Available params: See ProductFeedGetHotelsParams type.
    """
    return ProductFeed(productfeed_id).get_hotels(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def get_media_titles(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Media Titles for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve. Available fields: See MediaTitleField type.
        params: Query parameters. Available params: See ProductFeedGetMediaTitlesParams type.
    """
    return ProductFeed(productfeed_id).get_media_titles(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def get_products(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Products for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve. Available fields: See ProductItemField type.
        params: Query parameters. Available params: See ProductFeedGetProductsParams type.
    """
    return ProductFeed(productfeed_id).get_products(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def create_rule(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Rule for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductFeedCreateRuleParams type.
    """
    return ProductFeed(productfeed_id).create_rule(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def create_supplementary_feed_assoc(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Supplementary Feed Assoc for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductFeedCreateSupplementaryFeedAssocParams type.
    """
    return ProductFeed(productfeed_id).create_supplementary_feed_assoc(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def create_upload_schedule(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Upload Schedule for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductFeedCreateUploadScheduleParams type.
    """
    return ProductFeed(productfeed_id).create_upload_schedule(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def create_upload(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Upload for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductFeedCreateUploadParams type.
    """
    return ProductFeed(productfeed_id).create_upload(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def get_vehicle_offers(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Vehicle Offers for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve. Available fields: See VehicleOfferField type.
        params: Query parameters. Available params: See ProductFeedGetVehicleOffersParams type.
    """
    return ProductFeed(productfeed_id).get_vehicle_offers(fields=fields, params=params)


@productfeed_server.tool
@wrapped_fn_tool
def get_vehicles(
    productfeed_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Vehicles for this ProductFeed.

    Args:
        productfeed_id: The ID of the ProductFeed.
        fields: Fields to retrieve. Available fields: See VehicleField type.
        params: Query parameters. Available params: See ProductFeedGetVehiclesParams type.
    """
    return ProductFeed(productfeed_id).get_vehicles(fields=fields, params=params)
