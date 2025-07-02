"""
Auto-generated MCP server for Facebook ProductCatalog.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productcatalog import ProductCatalog
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productcatalog")


# CRUD Operations


@mcp.tool()
async def create_productcatalog(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = ProductCatalog(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = ProductCatalog(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ProductCatalog(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = ProductCatalog(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_agency_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Agency for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_agency result
    """
    result = ProductCatalog(fbid=object_id).create_agency(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_assigned_user_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Assigned User for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_assigned_user result
    """
    result = ProductCatalog(fbid=object_id).create_assigned_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_batch_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Batch for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_batch result
    """
    result = ProductCatalog(fbid=object_id).create_batch(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_catalog_store_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Catalog Store for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_catalog_store result
    """
    result = ProductCatalog(fbid=object_id).create_catalog_store(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_category_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Category for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_category result
    """
    result = ProductCatalog(fbid=object_id).create_category(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_cpas_lsb_image_bank_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Cpas Lsb Image Bank for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_cpas_lsb_image_bank result
    """
    result = ProductCatalog(fbid=object_id).create_cpas_lsb_image_bank(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_external_event_source_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create External Event Source for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_external_event_source result
    """
    result = ProductCatalog(fbid=object_id).create_external_event_source(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_geolocated_items_batch_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Geolocated Items Batch for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_geolocated_items_batch result
    """
    result = ProductCatalog(fbid=object_id).create_geolocated_items_batch(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_home_listing_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Home Listing for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_home_listing result
    """
    result = ProductCatalog(fbid=object_id).create_home_listing(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_hotel_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Hotel for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_hotel result
    """
    result = ProductCatalog(fbid=object_id).create_hotel(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_hotel_rooms_batch_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Hotel Rooms Batch for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_hotel_rooms_batch result
    """
    result = ProductCatalog(fbid=object_id).create_hotel_rooms_batch(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_items_batch_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Items Batch for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_items_batch result
    """
    result = ProductCatalog(fbid=object_id).create_items_batch(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_localized_items_batch_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Localized Items Batch for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_localized_items_batch result
    """
    result = ProductCatalog(fbid=object_id).create_localized_items_batch(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_market_place_partner_sellers_detail_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Market Place Partner Sellers Detail for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_market_place_partner_sellers_detail result
    """
    result = ProductCatalog(fbid=object_id).create_market_place_partner_sellers_detail(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_market_place_partner_signal_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Market Place Partner Signal for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_market_place_partner_signal result
    """
    result = ProductCatalog(fbid=object_id).create_market_place_partner_signal(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_pricing_variables_batch_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Pricing Variables Batch for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_pricing_variables_batch result
    """
    result = ProductCatalog(fbid=object_id).create_pricing_variables_batch(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_product_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Product for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_product result
    """
    result = ProductCatalog(fbid=object_id).create_product(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_product_feed_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Product Feed for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_product_feed result
    """
    result = ProductCatalog(fbid=object_id).create_product_feed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_product_group_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Product Group for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_product_group result
    """
    result = ProductCatalog(fbid=object_id).create_product_group(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_product_set_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Product Set for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_product_set result
    """
    result = ProductCatalog(fbid=object_id).create_product_set(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_update_generated_image_config_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Update Generated Image Config for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_update_generated_image_config result
    """
    result = ProductCatalog(fbid=object_id).create_update_generated_image_config(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_vehicle_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Vehicle for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_vehicle result
    """
    result = ProductCatalog(fbid=object_id).create_vehicle(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_version_items_batch_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Version Items Batch for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_version_items_batch result
    """
    result = ProductCatalog(fbid=object_id).create_version_items_batch(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_agencies_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Agencies for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_agencies result
    """
    result = ProductCatalog(fbid=object_id).delete_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_assigned_users_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Assigned Users for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_assigned_users result
    """
    result = ProductCatalog(fbid=object_id).delete_assigned_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_external_event_sources_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete External Event Sources for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_external_event_sources result
    """
    result = ProductCatalog(fbid=object_id).delete_external_event_sources(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_agencies_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Agencies for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_agencies result
    """
    result = ProductCatalog(fbid=object_id).get_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_users_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Assigned Users for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_assigned_users result
    """
    result = ProductCatalog(fbid=object_id).get_assigned_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_automotive_models_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Automotive Models for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_automotive_models result
    """
    result = ProductCatalog(fbid=object_id).get_automotive_models(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_categories_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Categories for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_categories result
    """
    result = ProductCatalog(fbid=object_id).get_categories(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_check_batch_request_status_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Check Batch Request Status for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_check_batch_request_status result
    """
    result = ProductCatalog(fbid=object_id).get_check_batch_request_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_check_marketplace_partner_sellers_status_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Check Marketplace Partner Sellers Status for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_check_marketplace_partner_sellers_status result
    """
    result = ProductCatalog(fbid=object_id).get_check_marketplace_partner_sellers_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_collaborative_ads_lsb_image_bank_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Collaborative Ads Lsb Image Bank for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_collaborative_ads_lsb_image_bank result
    """
    result = ProductCatalog(fbid=object_id).get_collaborative_ads_lsb_image_bank(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_collaborative_ads_share_settings_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Collaborative Ads Share Settings for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_collaborative_ads_share_settings result
    """
    result = ProductCatalog(fbid=object_id).get_collaborative_ads_share_settings(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_creator_asset_creatives_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Creator Asset Creatives for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_creator_asset_creatives result
    """
    result = ProductCatalog(fbid=object_id).get_creator_asset_creatives(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_data_sources_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Data Sources for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_data_sources result
    """
    result = ProductCatalog(fbid=object_id).get_data_sources(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_destinations_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Destinations for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_destinations result
    """
    result = ProductCatalog(fbid=object_id).get_destinations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_diagnostics_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Diagnostics for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_diagnostics result
    """
    result = ProductCatalog(fbid=object_id).get_diagnostics(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_event_stats_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Event Stats for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_event_stats result
    """
    result = ProductCatalog(fbid=object_id).get_event_stats(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_external_event_sources_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get External Event Sources for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_external_event_sources result
    """
    result = ProductCatalog(fbid=object_id).get_external_event_sources(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_flights_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Flights for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_flights result
    """
    result = ProductCatalog(fbid=object_id).get_flights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_home_listings_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Home Listings for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_home_listings result
    """
    result = ProductCatalog(fbid=object_id).get_home_listings(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_hotel_rooms_batch_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Hotel Rooms Batch for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_hotel_rooms_batch result
    """
    result = ProductCatalog(fbid=object_id).get_hotel_rooms_batch(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_hotels_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Hotels for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_hotels result
    """
    result = ProductCatalog(fbid=object_id).get_hotels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pricing_variables_batch_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Pricing Variables Batch for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_pricing_variables_batch result
    """
    result = ProductCatalog(fbid=object_id).get_pricing_variables_batch(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_product_feeds_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Product Feeds for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_product_feeds result
    """
    result = ProductCatalog(fbid=object_id).get_product_feeds(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_product_groups_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Product Groups for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_product_groups result
    """
    result = ProductCatalog(fbid=object_id).get_product_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_product_sets_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Product Sets for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_product_sets result
    """
    result = ProductCatalog(fbid=object_id).get_product_sets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_product_sets_batch_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Product Sets Batch for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_product_sets_batch result
    """
    result = ProductCatalog(fbid=object_id).get_product_sets_batch(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_products_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Products for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_products result
    """
    result = ProductCatalog(fbid=object_id).get_products(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_vehicle_offers_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Vehicle Offers for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_vehicle_offers result
    """
    result = ProductCatalog(fbid=object_id).get_vehicle_offers(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_vehicles_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Vehicles for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_vehicles result
    """
    result = ProductCatalog(fbid=object_id).get_vehicles(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_version_configs_for_productcatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Version Configs for ProductCatalog.

    Args:
        object_id: The ID of the ProductCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_version_configs result
    """
    result = ProductCatalog(fbid=object_id).get_version_configs(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productcatalog_server = mcp
