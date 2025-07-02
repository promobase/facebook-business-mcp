"""
Auto-generated MCP server for Facebook ProductFeed.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productfeed import ProductFeed
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productfeed")


# CRUD Operations


@mcp.tool()
async def create_productfeed(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = ProductFeed(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = ProductFeed(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ProductFeed(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = ProductFeed(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_rule_for_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Rule for ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_rule result
    """
    result = ProductFeed(fbid=object_id).create_rule(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_supplementary_feed_assoc_for_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Supplementary Feed Assoc for ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_supplementary_feed_assoc result
    """
    result = ProductFeed(fbid=object_id).create_supplementary_feed_assoc(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_upload_for_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Upload for ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_upload result
    """
    result = ProductFeed(fbid=object_id).create_upload(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_upload_schedule_for_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Upload Schedule for ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_upload_schedule result
    """
    result = ProductFeed(fbid=object_id).create_upload_schedule(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_automotive_models_for_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Automotive Models for ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_automotive_models result
    """
    result = ProductFeed(fbid=object_id).get_automotive_models(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_destinations_for_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Destinations for ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_destinations result
    """
    result = ProductFeed(fbid=object_id).get_destinations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_flights_for_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Flights for ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_flights result
    """
    result = ProductFeed(fbid=object_id).get_flights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_home_listings_for_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Home Listings for ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_home_listings result
    """
    result = ProductFeed(fbid=object_id).get_home_listings(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_hotels_for_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Hotels for ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_hotels result
    """
    result = ProductFeed(fbid=object_id).get_hotels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_media_titles_for_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Media Titles for ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_media_titles result
    """
    result = ProductFeed(fbid=object_id).get_media_titles(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_products_for_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Products for ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_products result
    """
    result = ProductFeed(fbid=object_id).get_products(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_rules_for_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Rules for ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_rules result
    """
    result = ProductFeed(fbid=object_id).get_rules(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_upload_schedules_for_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Upload Schedules for ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_upload_schedules result
    """
    result = ProductFeed(fbid=object_id).get_upload_schedules(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_uploads_for_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Uploads for ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_uploads result
    """
    result = ProductFeed(fbid=object_id).get_uploads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_vehicle_offers_for_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Vehicle Offers for ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_vehicle_offers result
    """
    result = ProductFeed(fbid=object_id).get_vehicle_offers(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_vehicles_for_productfeed(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Vehicles for ProductFeed.

    Args:
        object_id: The ID of the ProductFeed
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_vehicles result
    """
    result = ProductFeed(fbid=object_id).get_vehicles(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productfeed_server = mcp
