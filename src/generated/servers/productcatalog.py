"""ProductCatalog MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.productcatalog import ProductCatalog
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.assigneduser import AssignedUserField
from src.generated.models.automotivemodel import AutomotiveModelField
from src.generated.models.checkbatchrequeststatus import CheckBatchRequestStatusField
from src.generated.models.cpaslsbimagebank import CPASLsbImageBankField
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
from src.generated.models.productfeed import ProductFeedField
from src.generated.models.productgroup import ProductGroupField
from src.generated.models.productitem import ProductItemField
from src.generated.models.productset import ProductSetField
from src.generated.models.storecatalogsettings import StoreCatalogSettingsField
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
@productcatalog_server.tool
@wrapped_fn_tool
def get_productcatalog(
    productcatalog_id: str,
    fields: list[ProductCatalogField] = [],
) -> str:
    """Get a ProductCatalog object by ID.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See ProductCatalogField type.
    """
    obj = ProductCatalog(productcatalog_id)
    return obj.api_get(fields=fields)


@productcatalog_server.tool
@wrapped_fn_tool
def update_productcatalog(
    productcatalog_id: str,
    fields: list[ProductCatalogField] = [],
    params: ProductCatalogUpdateParams | dict = {},
) -> str:
    """Update a ProductCatalog object.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to return after update. Available fields: See ProductCatalogField type.
        params: Parameters to update. Available params: See ProductCatalogUpdateParams type.
    """
    return ProductCatalog(productcatalog_id).api_update(fields=fields, params=params)


@productcatalog_server.tool
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
@productcatalog_server.tool
@wrapped_fn_tool
def delete_agencies(
    productcatalog_id: str,
    params: ProductCatalogDeleteAgenciesParams | dict = {},
):
    """Delete Agencies for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        params: Query parameters. Available params: See ProductCatalogDeleteAgenciesParams type.
    """
    return ProductCatalog(productcatalog_id).delete_agencies(params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_agency(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateAgencyParams | dict = {},
):
    """Create Agency for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateAgencyParams type.
    """
    return ProductCatalog(productcatalog_id).create_agency(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def delete_assigned_users(
    productcatalog_id: str,
    params: ProductCatalogDeleteAssignedUsersParams | dict = {},
):
    """Delete Assigned Users for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        params: Query parameters. Available params: See ProductCatalogDeleteAssignedUsersParams type.
    """
    return ProductCatalog(productcatalog_id).delete_assigned_users(params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_assigned_users(
    productcatalog_id: str,
    fields: list[AssignedUserField] = [],
    params: ProductCatalogGetAssignedUsersParams | dict = {},
):
    """Get Assigned Users for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See AssignedUserField type.
        params: Query parameters. Available params: See ProductCatalogGetAssignedUsersParams type.
    """
    return ProductCatalog(productcatalog_id).get_assigned_users(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_assigned_user(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateAssignedUserParams | dict = {},
):
    """Create Assigned User for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateAssignedUserParams type.
    """
    return ProductCatalog(productcatalog_id).create_assigned_user(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_automotive_models(
    productcatalog_id: str,
    fields: list[AutomotiveModelField] = [],
    params: ProductCatalogGetAutomotiveModelsParams | dict = {},
):
    """Get Automotive Models for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See AutomotiveModelField type.
        params: Query parameters. Available params: See ProductCatalogGetAutomotiveModelsParams type.
    """
    return ProductCatalog(productcatalog_id).get_automotive_models(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateBatchParams | dict = {},
):
    """Create Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateBatchParams type.
    """
    return ProductCatalog(productcatalog_id).create_batch(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_catalog_store(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateCatalogStoreParams | dict = {},
):
    """Create Catalog Store for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateCatalogStoreParams type.
    """
    return ProductCatalog(productcatalog_id).create_catalog_store(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_categories(
    productcatalog_id: str,
    fields: list[ProductCatalogCategoryField] = [],
    params: ProductCatalogGetCategoriesParams | dict = {},
):
    """Get Categories for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See ProductCatalogCategoryField type.
        params: Query parameters. Available params: See ProductCatalogGetCategoriesParams type.
    """
    return ProductCatalog(productcatalog_id).get_categories(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_category(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateCategoryParams | dict = {},
):
    """Create Category for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateCategoryParams type.
    """
    return ProductCatalog(productcatalog_id).create_category(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_check_batch_request_status(
    productcatalog_id: str,
    fields: list[CheckBatchRequestStatusField] = [],
    params: ProductCatalogGetCheckBatchRequestStatusParams | dict = {},
):
    """Get Check Batch Request Status for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See CheckBatchRequestStatusField type.
        params: Query parameters. Available params: See ProductCatalogGetCheckBatchRequestStatusParams type.
    """
    return ProductCatalog(productcatalog_id).get_check_batch_request_status(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def get_check_marketplace_partner_sellers_status(
    productcatalog_id: str,
    fields: list[ProductCatalogCheckMarketplacePartnerSellersStatusField] = [],
    params: ProductCatalogGetCheckMarketplacePartnerSellersStatusParams | dict = {},
):
    """Get Check Marketplace Partner Sellers Status for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See ProductCatalogCheckMarketplacePartnerSellersStatusField type.
        params: Query parameters. Available params: See ProductCatalogGetCheckMarketplacePartnerSellersStatusParams type.
    """
    return ProductCatalog(productcatalog_id).get_check_marketplace_partner_sellers_status(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def create_cpas_lsb_image_bank(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateCpasLsbImageBankParams | dict = {},
):
    """Create Cpas Lsb Image Bank for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateCpasLsbImageBankParams type.
    """
    return ProductCatalog(productcatalog_id).create_cpas_lsb_image_bank(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def get_creator_asset_creatives(
    productcatalog_id: str,
    fields: list[CreatorAssetCreativeField] = [],
    params: ProductCatalogGetCreatorAssetCreativesParams | dict = {},
):
    """Get Creator Asset Creatives for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See CreatorAssetCreativeField type.
        params: Query parameters. Available params: See ProductCatalogGetCreatorAssetCreativesParams type.
    """
    return ProductCatalog(productcatalog_id).get_creator_asset_creatives(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def get_data_sources(
    productcatalog_id: str,
    fields: list[ProductCatalogDataSourceField] = [],
    params: ProductCatalogGetDataSourcesParams | dict = {},
):
    """Get Data Sources for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See ProductCatalogDataSourceField type.
        params: Query parameters. Available params: See ProductCatalogGetDataSourcesParams type.
    """
    return ProductCatalog(productcatalog_id).get_data_sources(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_destinations(
    productcatalog_id: str,
    fields: list[DestinationField] = [],
    params: ProductCatalogGetDestinationsParams | dict = {},
):
    """Get Destinations for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See DestinationField type.
        params: Query parameters. Available params: See ProductCatalogGetDestinationsParams type.
    """
    return ProductCatalog(productcatalog_id).get_destinations(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_diagnostics(
    productcatalog_id: str,
    fields: list[ProductCatalogDiagnosticGroupField] = [],
    params: ProductCatalogGetDiagnosticsParams | dict = {},
):
    """Get Diagnostics for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See ProductCatalogDiagnosticGroupField type.
        params: Query parameters. Available params: See ProductCatalogGetDiagnosticsParams type.
    """
    return ProductCatalog(productcatalog_id).get_diagnostics(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_event_stats(
    productcatalog_id: str,
    fields: list[ProductEventStatField] = [],
    params: ProductCatalogGetEventStatsParams | dict = {},
):
    """Get Event Stats for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See ProductEventStatField type.
        params: Query parameters. Available params: See ProductCatalogGetEventStatsParams type.
    """
    return ProductCatalog(productcatalog_id).get_event_stats(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def delete_external_event_sources(
    productcatalog_id: str,
    params: ProductCatalogDeleteExternalEventSourcesParams | dict = {},
):
    """Delete External Event Sources for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        params: Query parameters. Available params: See ProductCatalogDeleteExternalEventSourcesParams type.
    """
    return ProductCatalog(productcatalog_id).delete_external_event_sources(params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_external_event_source(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateExternalEventSourceParams | dict = {},
):
    """Create External Event Source for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateExternalEventSourceParams type.
    """
    return ProductCatalog(productcatalog_id).create_external_event_source(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def get_flights(
    productcatalog_id: str,
    fields: list[FlightField] = [],
    params: ProductCatalogGetFlightsParams | dict = {},
):
    """Get Flights for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See FlightField type.
        params: Query parameters. Available params: See ProductCatalogGetFlightsParams type.
    """
    return ProductCatalog(productcatalog_id).get_flights(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_geolocated_items_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateGeolocatedItemsBatchParams | dict = {},
):
    """Create Geolocated Items Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateGeolocatedItemsBatchParams type.
    """
    return ProductCatalog(productcatalog_id).create_geolocated_items_batch(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def get_home_listings(
    productcatalog_id: str,
    fields: list[HomeListingField] = [],
    params: ProductCatalogGetHomeListingsParams | dict = {},
):
    """Get Home Listings for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See HomeListingField type.
        params: Query parameters. Available params: See ProductCatalogGetHomeListingsParams type.
    """
    return ProductCatalog(productcatalog_id).get_home_listings(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_home_listing(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateHomeListingParams | dict = {},
):
    """Create Home Listing for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateHomeListingParams type.
    """
    return ProductCatalog(productcatalog_id).create_home_listing(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_hotel_rooms_batch(
    productcatalog_id: str,
    fields: list[ProductCatalogHotelRoomsBatchField] = [],
    params: ProductCatalogGetHotelRoomsBatchParams | dict = {},
):
    """Get Hotel Rooms Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See ProductCatalogHotelRoomsBatchField type.
        params: Query parameters. Available params: See ProductCatalogGetHotelRoomsBatchParams type.
    """
    return ProductCatalog(productcatalog_id).get_hotel_rooms_batch(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_hotel_rooms_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateHotelRoomsBatchParams | dict = {},
):
    """Create Hotel Rooms Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateHotelRoomsBatchParams type.
    """
    return ProductCatalog(productcatalog_id).create_hotel_rooms_batch(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_hotels(
    productcatalog_id: str,
    fields: list[HotelField] = [],
    params: ProductCatalogGetHotelsParams | dict = {},
):
    """Get Hotels for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See HotelField type.
        params: Query parameters. Available params: See ProductCatalogGetHotelsParams type.
    """
    return ProductCatalog(productcatalog_id).get_hotels(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_hotel(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateHotelParams | dict = {},
):
    """Create Hotel for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateHotelParams type.
    """
    return ProductCatalog(productcatalog_id).create_hotel(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_items_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateItemsBatchParams | dict = {},
):
    """Create Items Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateItemsBatchParams type.
    """
    return ProductCatalog(productcatalog_id).create_items_batch(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_localized_items_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateLocalizedItemsBatchParams | dict = {},
):
    """Create Localized Items Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateLocalizedItemsBatchParams type.
    """
    return ProductCatalog(productcatalog_id).create_localized_items_batch(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def create_market_place_partner_sellers_detail(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateMarketPlacePartnerSellersDetailParams | dict = {},
):
    """Create Market Place Partner Sellers Detail for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateMarketPlacePartnerSellersDetailParams type.
    """
    return ProductCatalog(productcatalog_id).create_market_place_partner_sellers_detail(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def create_market_place_partner_signal(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateMarketPlacePartnerSignalParams | dict = {},
):
    """Create Market Place Partner Signal for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateMarketPlacePartnerSignalParams type.
    """
    return ProductCatalog(productcatalog_id).create_market_place_partner_signal(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def get_pricing_variables_batch(
    productcatalog_id: str,
    fields: list[ProductCatalogPricingVariablesBatchField] = [],
    params: ProductCatalogGetPricingVariablesBatchParams | dict = {},
):
    """Get Pricing Variables Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See ProductCatalogPricingVariablesBatchField type.
        params: Query parameters. Available params: See ProductCatalogGetPricingVariablesBatchParams type.
    """
    return ProductCatalog(productcatalog_id).get_pricing_variables_batch(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def create_pricing_variables_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreatePricingVariablesBatchParams | dict = {},
):
    """Create Pricing Variables Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreatePricingVariablesBatchParams type.
    """
    return ProductCatalog(productcatalog_id).create_pricing_variables_batch(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def create_product_feed(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateProductFeedParams | dict = {},
):
    """Create Product Feed for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateProductFeedParams type.
    """
    return ProductCatalog(productcatalog_id).create_product_feed(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_product_group(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateProductGroupParams | dict = {},
):
    """Create Product Group for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateProductGroupParams type.
    """
    return ProductCatalog(productcatalog_id).create_product_group(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_product_sets(
    productcatalog_id: str,
    fields: list[ProductSetField] = [],
    params: ProductCatalogGetProductSetsParams | dict = {},
):
    """Get Product Sets for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See ProductSetField type.
        params: Query parameters. Available params: See ProductCatalogGetProductSetsParams type.
    """
    return ProductCatalog(productcatalog_id).get_product_sets(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_product_set(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateProductSetParams | dict = {},
):
    """Create Product Set for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateProductSetParams type.
    """
    return ProductCatalog(productcatalog_id).create_product_set(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_product_sets_batch(
    productcatalog_id: str,
    fields: list[ProductCatalogProductSetsBatchField] = [],
    params: ProductCatalogGetProductSetsBatchParams | dict = {},
):
    """Get Product Sets Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See ProductCatalogProductSetsBatchField type.
        params: Query parameters. Available params: See ProductCatalogGetProductSetsBatchParams type.
    """
    return ProductCatalog(productcatalog_id).get_product_sets_batch(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_products(
    productcatalog_id: str,
    fields: list[ProductItemField] = [],
    params: ProductCatalogGetProductsParams | dict = {},
):
    """Get Products for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See ProductItemField type.
        params: Query parameters. Available params: See ProductCatalogGetProductsParams type.
    """
    return ProductCatalog(productcatalog_id).get_products(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_product(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateProductParams | dict = {},
):
    """Create Product for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateProductParams type.
    """
    return ProductCatalog(productcatalog_id).create_product(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_update_generated_image_config(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateUpdateGeneratedImageConfigParams | dict = {},
):
    """Create Update Generated Image Config for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateUpdateGeneratedImageConfigParams type.
    """
    return ProductCatalog(productcatalog_id).create_update_generated_image_config(
        fields=fields, params=params
    )


@productcatalog_server.tool
@wrapped_fn_tool
def get_vehicle_offers(
    productcatalog_id: str,
    fields: list[VehicleOfferField] = [],
    params: ProductCatalogGetVehicleOffersParams | dict = {},
):
    """Get Vehicle Offers for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See VehicleOfferField type.
        params: Query parameters. Available params: See ProductCatalogGetVehicleOffersParams type.
    """
    return ProductCatalog(productcatalog_id).get_vehicle_offers(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def get_vehicles(
    productcatalog_id: str,
    fields: list[VehicleField] = [],
    params: ProductCatalogGetVehiclesParams | dict = {},
):
    """Get Vehicles for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve. Available fields: See VehicleField type.
        params: Query parameters. Available params: See ProductCatalogGetVehiclesParams type.
    """
    return ProductCatalog(productcatalog_id).get_vehicles(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_vehicle(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateVehicleParams | dict = {},
):
    """Create Vehicle for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateVehicleParams type.
    """
    return ProductCatalog(productcatalog_id).create_vehicle(fields=fields, params=params)


@productcatalog_server.tool
@wrapped_fn_tool
def create_version_items_batch(
    productcatalog_id: str,
    fields: list[str] = [],
    params: ProductCatalogCreateVersionItemsBatchParams | dict = {},
):
    """Create Version Items Batch for this ProductCatalog.

    Args:
        productcatalog_id: The ID of the ProductCatalog.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See ProductCatalogCreateVersionItemsBatchParams type.
    """
    return ProductCatalog(productcatalog_id).create_version_items_batch(
        fields=fields, params=params
    )
