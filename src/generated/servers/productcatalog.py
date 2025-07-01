"""ProductCatalog MCP Server with typed wrappers."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.productcatalog import ProductCatalog
from fastmcp import FastMCP

from src.generated.models.assigneduser import AssignedUserField
from src.generated.models.automotivemodel import AutomotiveModelField
from src.generated.models.checkbatchrequeststatus import CheckBatchRequestStatusField
from src.generated.models.creatorassetcreative import CreatorAssetCreativeField
from src.generated.models.destination import DestinationField
from src.generated.models.flight import FlightField
from src.generated.models.homelisting import HomeListingField
from src.generated.models.hotel import HotelField
from src.generated.models.productcatalog import (
    ProductCatalogCreateAgencyParams,
    ProductCatalogCreateAssignedUserParams,
    ProductCatalogCreateBatchParams,
    ProductCatalogCreateCatalogStoreParams,
    ProductCatalogCreateCategoryParams,
    ProductCatalogCreateCpasLsbImageBankParams,
    ProductCatalogCreateExternalEventSourceParams,
    ProductCatalogCreateGeolocatedItemsBatchParams,
    ProductCatalogCreateHomeListingParams,
    ProductCatalogCreateHotelParams,
    ProductCatalogCreateHotelRoomsBatchParams,
    ProductCatalogCreateItemsBatchParams,
    ProductCatalogCreateLocalizedItemsBatchParams,
    ProductCatalogCreateMarketPlacePartnerSellersDetailParams,
    ProductCatalogCreateMarketPlacePartnerSignalParams,
    ProductCatalogCreatePricingVariablesBatchParams,
    ProductCatalogCreateProductFeedParams,
    ProductCatalogCreateProductGroupParams,
    ProductCatalogCreateProductParams,
    ProductCatalogCreateProductSetParams,
    ProductCatalogCreateUpdateGeneratedImageConfigParams,
    ProductCatalogCreateVehicleParams,
    ProductCatalogCreateVersionItemsBatchParams,
    ProductCatalogDeleteAgenciesParams,
    ProductCatalogDeleteAssignedUsersParams,
    ProductCatalogDeleteExternalEventSourcesParams,
    ProductCatalogField,
    ProductCatalogGetAssignedUsersParams,
    ProductCatalogGetAutomotiveModelsParams,
    ProductCatalogGetCategoriesParams,
    ProductCatalogGetCheckBatchRequestStatusParams,
    ProductCatalogGetCheckMarketplacePartnerSellersStatusParams,
    ProductCatalogGetCreatorAssetCreativesParams,
    ProductCatalogGetDataSourcesParams,
    ProductCatalogGetDestinationsParams,
    ProductCatalogGetDiagnosticsParams,
    ProductCatalogGetEventStatsParams,
    ProductCatalogGetFlightsParams,
    ProductCatalogGetHomeListingsParams,
    ProductCatalogGetHotelRoomsBatchParams,
    ProductCatalogGetHotelsParams,
    ProductCatalogGetPricingVariablesBatchParams,
    ProductCatalogGetProductSetsBatchParams,
    ProductCatalogGetProductSetsParams,
    ProductCatalogGetProductsParams,
    ProductCatalogGetVehicleOffersParams,
    ProductCatalogGetVehiclesParams,
    ProductCatalogUpdateParams,
)
from src.generated.models.productcatalogcategory import ProductCatalogCategoryField
from src.generated.models.productcatalogcheckmarketplacepartnersellersstatus import (
    ProductCatalogCheckMarketplacePartnerSellersStatusField,
)
from src.generated.models.productcatalogdatasource import ProductCatalogDataSourceField
from src.generated.models.productcatalogdiagnosticgroup import ProductCatalogDiagnosticGroupField
from src.generated.models.productcataloghotelroomsbatch import ProductCatalogHotelRoomsBatchField
from src.generated.models.productcatalogpricingvariablesbatch import (
    ProductCatalogPricingVariablesBatchField,
)
from src.generated.models.productcatalogproductsetsbatch import ProductCatalogProductSetsBatchField
from src.generated.models.producteventstat import ProductEventStatField
from src.generated.models.productitem import ProductItemField
from src.generated.models.productset import ProductSetField
from src.generated.models.vehicle import VehicleField
from src.generated.models.vehicleoffer import VehicleOfferField
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


productcatalog_server.tool(get_productcatalog)


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


productcatalog_server.tool(update_productcatalog)


@wrapped_fn_tool
def delete_productcatalog(
    productcatalog_id: str,
) -> str:
    """Delete a ProductCatalog object.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
    """
    return ProductCatalog(productcatalog_id).api_delete()


productcatalog_server.tool(delete_productcatalog)


# ---- Edge Methods (46) ----
@wrapped_fn_tool
def delete_agencies(
    productcatalog_id: str,
    params: ProductCatalogDeleteAgenciesParams = {},
) -> Any:
    """Delete Agencies for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).delete_agencies(params=params)


productcatalog_server.tool(delete_agencies)


@wrapped_fn_tool
def create_agency(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateAgencyParams = {},
) -> Any:
    """Create Agency for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_agency(fields=fields, params=params)


productcatalog_server.tool(create_agency)


@wrapped_fn_tool
def delete_assigned_users(
    productcatalog_id: str,
    params: ProductCatalogDeleteAssignedUsersParams = {},
) -> Any:
    """Delete Assigned Users for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).delete_assigned_users(params=params)


productcatalog_server.tool(delete_assigned_users)


@wrapped_fn_tool
def get_assigned_users(
    productcatalog_id: str,
    fields: list[AssignedUserField] = [],
    params: ProductCatalogGetAssignedUsersParams = {},
) -> Any:
    """Get Assigned Users for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_assigned_users(fields=fields, params=params)


productcatalog_server.tool(get_assigned_users)


@wrapped_fn_tool
def create_assigned_user(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateAssignedUserParams = {},
) -> Any:
    """Create Assigned User for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_assigned_user(fields=fields, params=params)


productcatalog_server.tool(create_assigned_user)


@wrapped_fn_tool
def get_automotive_models(
    productcatalog_id: str,
    fields: list[AutomotiveModelField] = [],
    params: ProductCatalogGetAutomotiveModelsParams = {},
) -> Any:
    """Get Automotive Models for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_automotive_models(fields=fields, params=params)


productcatalog_server.tool(get_automotive_models)


@wrapped_fn_tool
def create_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateBatchParams = {},
) -> Any:
    """Create Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_batch(fields=fields, params=params)


productcatalog_server.tool(create_batch)


@wrapped_fn_tool
def create_catalog_store(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateCatalogStoreParams = {},
) -> Any:
    """Create Catalog Store for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_catalog_store(fields=fields, params=params)


productcatalog_server.tool(create_catalog_store)


@wrapped_fn_tool
def get_categories(
    productcatalog_id: str,
    fields: list[ProductCatalogCategoryField] = [],
    params: ProductCatalogGetCategoriesParams = {},
) -> Any:
    """Get Categories for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_categories(fields=fields, params=params)


productcatalog_server.tool(get_categories)


@wrapped_fn_tool
def create_category(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateCategoryParams = {},
) -> Any:
    """Create Category for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_category(fields=fields, params=params)


productcatalog_server.tool(create_category)


@wrapped_fn_tool
def get_check_batch_request_status(
    productcatalog_id: str,
    fields: list[CheckBatchRequestStatusField] = [],
    params: ProductCatalogGetCheckBatchRequestStatusParams = {},
) -> Any:
    """Get Check Batch Request Status for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_check_batch_request_status(
        fields=fields, params=params
    )


productcatalog_server.tool(get_check_batch_request_status)


@wrapped_fn_tool
def get_check_marketplace_partner_sellers_status(
    productcatalog_id: str,
    fields: list[ProductCatalogCheckMarketplacePartnerSellersStatusField] = [],
    params: ProductCatalogGetCheckMarketplacePartnerSellersStatusParams = {},
) -> Any:
    """Get Check Marketplace Partner Sellers Status for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_check_marketplace_partner_sellers_status(
        fields=fields, params=params
    )


productcatalog_server.tool(get_check_marketplace_partner_sellers_status)


@wrapped_fn_tool
def create_cpas_lsb_image_bank(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateCpasLsbImageBankParams = {},
) -> Any:
    """Create Cpas Lsb Image Bank for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_cpas_lsb_image_bank(
        fields=fields, params=params
    )


productcatalog_server.tool(create_cpas_lsb_image_bank)


@wrapped_fn_tool
def get_creator_asset_creatives(
    productcatalog_id: str,
    fields: list[CreatorAssetCreativeField] = [],
    params: ProductCatalogGetCreatorAssetCreativesParams = {},
) -> Any:
    """Get Creator Asset Creatives for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_creator_asset_creatives(
        fields=fields, params=params
    )


productcatalog_server.tool(get_creator_asset_creatives)


@wrapped_fn_tool
def get_data_sources(
    productcatalog_id: str,
    fields: list[ProductCatalogDataSourceField] = [],
    params: ProductCatalogGetDataSourcesParams = {},
) -> Any:
    """Get Data Sources for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_data_sources(fields=fields, params=params)


productcatalog_server.tool(get_data_sources)


@wrapped_fn_tool
def get_destinations(
    productcatalog_id: str,
    fields: list[DestinationField] = [],
    params: ProductCatalogGetDestinationsParams = {},
) -> Any:
    """Get Destinations for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_destinations(fields=fields, params=params)


productcatalog_server.tool(get_destinations)


@wrapped_fn_tool
def get_diagnostics(
    productcatalog_id: str,
    fields: list[ProductCatalogDiagnosticGroupField] = [],
    params: ProductCatalogGetDiagnosticsParams = {},
) -> Any:
    """Get Diagnostics for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_diagnostics(fields=fields, params=params)


productcatalog_server.tool(get_diagnostics)


@wrapped_fn_tool
def get_event_stats(
    productcatalog_id: str,
    fields: list[ProductEventStatField] = [],
    params: ProductCatalogGetEventStatsParams = {},
) -> Any:
    """Get Event Stats for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_event_stats(fields=fields, params=params)


productcatalog_server.tool(get_event_stats)


@wrapped_fn_tool
def delete_external_event_sources(
    productcatalog_id: str,
    params: ProductCatalogDeleteExternalEventSourcesParams = {},
) -> Any:
    """Delete External Event Sources for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).delete_external_event_sources(params=params)


productcatalog_server.tool(delete_external_event_sources)


@wrapped_fn_tool
def create_external_event_source(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateExternalEventSourceParams = {},
) -> Any:
    """Create External Event Source for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_external_event_source(
        fields=fields, params=params
    )


productcatalog_server.tool(create_external_event_source)


@wrapped_fn_tool
def get_flights(
    productcatalog_id: str,
    fields: list[FlightField] = [],
    params: ProductCatalogGetFlightsParams = {},
) -> Any:
    """Get Flights for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_flights(fields=fields, params=params)


productcatalog_server.tool(get_flights)


@wrapped_fn_tool
def create_geolocated_items_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateGeolocatedItemsBatchParams = {},
) -> Any:
    """Create Geolocated Items Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_geolocated_items_batch(
        fields=fields, params=params
    )


productcatalog_server.tool(create_geolocated_items_batch)


@wrapped_fn_tool
def get_home_listings(
    productcatalog_id: str,
    fields: list[HomeListingField] = [],
    params: ProductCatalogGetHomeListingsParams = {},
) -> Any:
    """Get Home Listings for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_home_listings(fields=fields, params=params)


productcatalog_server.tool(get_home_listings)


@wrapped_fn_tool
def create_home_listing(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateHomeListingParams = {},
) -> Any:
    """Create Home Listing for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_home_listing(fields=fields, params=params)


productcatalog_server.tool(create_home_listing)


@wrapped_fn_tool
def get_hotel_rooms_batch(
    productcatalog_id: str,
    fields: list[ProductCatalogHotelRoomsBatchField] = [],
    params: ProductCatalogGetHotelRoomsBatchParams = {},
) -> Any:
    """Get Hotel Rooms Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_hotel_rooms_batch(fields=fields, params=params)


productcatalog_server.tool(get_hotel_rooms_batch)


@wrapped_fn_tool
def create_hotel_rooms_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateHotelRoomsBatchParams = {},
) -> Any:
    """Create Hotel Rooms Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_hotel_rooms_batch(fields=fields, params=params)


productcatalog_server.tool(create_hotel_rooms_batch)


@wrapped_fn_tool
def get_hotels(
    productcatalog_id: str,
    fields: list[HotelField] = [],
    params: ProductCatalogGetHotelsParams = {},
) -> Any:
    """Get Hotels for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_hotels(fields=fields, params=params)


productcatalog_server.tool(get_hotels)


@wrapped_fn_tool
def create_hotel(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateHotelParams = {},
) -> Any:
    """Create Hotel for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_hotel(fields=fields, params=params)


productcatalog_server.tool(create_hotel)


@wrapped_fn_tool
def create_items_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateItemsBatchParams = {},
) -> Any:
    """Create Items Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_items_batch(fields=fields, params=params)


productcatalog_server.tool(create_items_batch)


@wrapped_fn_tool
def create_localized_items_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateLocalizedItemsBatchParams = {},
) -> Any:
    """Create Localized Items Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_localized_items_batch(
        fields=fields, params=params
    )


productcatalog_server.tool(create_localized_items_batch)


@wrapped_fn_tool
def create_market_place_partner_sellers_detail(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateMarketPlacePartnerSellersDetailParams = {},
) -> Any:
    """Create Market Place Partner Sellers Detail for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_market_place_partner_sellers_detail(
        fields=fields, params=params
    )


productcatalog_server.tool(create_market_place_partner_sellers_detail)


@wrapped_fn_tool
def create_market_place_partner_signal(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateMarketPlacePartnerSignalParams = {},
) -> Any:
    """Create Market Place Partner Signal for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_market_place_partner_signal(
        fields=fields, params=params
    )


productcatalog_server.tool(create_market_place_partner_signal)


@wrapped_fn_tool
def get_pricing_variables_batch(
    productcatalog_id: str,
    fields: list[ProductCatalogPricingVariablesBatchField] = [],
    params: ProductCatalogGetPricingVariablesBatchParams = {},
) -> Any:
    """Get Pricing Variables Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_pricing_variables_batch(
        fields=fields, params=params
    )


productcatalog_server.tool(get_pricing_variables_batch)


@wrapped_fn_tool
def create_pricing_variables_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreatePricingVariablesBatchParams = {},
) -> Any:
    """Create Pricing Variables Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_pricing_variables_batch(
        fields=fields, params=params
    )


productcatalog_server.tool(create_pricing_variables_batch)


@wrapped_fn_tool
def create_product_feed(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateProductFeedParams = {},
) -> Any:
    """Create Product Feed for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_product_feed(fields=fields, params=params)


productcatalog_server.tool(create_product_feed)


@wrapped_fn_tool
def create_product_group(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateProductGroupParams = {},
) -> Any:
    """Create Product Group for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_product_group(fields=fields, params=params)


productcatalog_server.tool(create_product_group)


@wrapped_fn_tool
def get_product_sets(
    productcatalog_id: str,
    fields: list[ProductSetField] = [],
    params: ProductCatalogGetProductSetsParams = {},
) -> Any:
    """Get Product Sets for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_product_sets(fields=fields, params=params)


productcatalog_server.tool(get_product_sets)


@wrapped_fn_tool
def create_product_set(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateProductSetParams = {},
) -> Any:
    """Create Product Set for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_product_set(fields=fields, params=params)


productcatalog_server.tool(create_product_set)


@wrapped_fn_tool
def get_product_sets_batch(
    productcatalog_id: str,
    fields: list[ProductCatalogProductSetsBatchField] = [],
    params: ProductCatalogGetProductSetsBatchParams = {},
) -> Any:
    """Get Product Sets Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_product_sets_batch(fields=fields, params=params)


productcatalog_server.tool(get_product_sets_batch)


@wrapped_fn_tool
def get_products(
    productcatalog_id: str,
    fields: list[ProductItemField] = [],
    params: ProductCatalogGetProductsParams = {},
) -> Any:
    """Get Products for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_products(fields=fields, params=params)


productcatalog_server.tool(get_products)


@wrapped_fn_tool
def create_product(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateProductParams = {},
) -> Any:
    """Create Product for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_product(fields=fields, params=params)


productcatalog_server.tool(create_product)


@wrapped_fn_tool
def create_update_generated_image_config(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateUpdateGeneratedImageConfigParams = {},
) -> Any:
    """Create Update Generated Image Config for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_update_generated_image_config(
        fields=fields, params=params
    )


productcatalog_server.tool(create_update_generated_image_config)


@wrapped_fn_tool
def get_vehicle_offers(
    productcatalog_id: str,
    fields: list[VehicleOfferField] = [],
    params: ProductCatalogGetVehicleOffersParams = {},
) -> Any:
    """Get Vehicle Offers for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_vehicle_offers(fields=fields, params=params)


productcatalog_server.tool(get_vehicle_offers)


@wrapped_fn_tool
def get_vehicles(
    productcatalog_id: str,
    fields: list[VehicleField] = [],
    params: ProductCatalogGetVehiclesParams = {},
) -> Any:
    """Get Vehicles for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).get_vehicles(fields=fields, params=params)


productcatalog_server.tool(get_vehicles)


@wrapped_fn_tool
def create_vehicle(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateVehicleParams = {},
) -> Any:
    """Create Vehicle for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_vehicle(fields=fields, params=params)


productcatalog_server.tool(create_vehicle)


@wrapped_fn_tool
def create_version_items_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateVersionItemsBatchParams = {},
) -> Any:
    """Create Version Items Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return ProductCatalog(productcatalog_id).create_version_items_batch(
        fields=fields, params=params
    )


productcatalog_server.tool(create_version_items_batch)
