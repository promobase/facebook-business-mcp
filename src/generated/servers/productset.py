"""
Auto-generated MCP server for Facebook ProductSet.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productset import ProductSet
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productset")


# CRUD Operations


@mcp.tool()
async def create_productset(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a ProductSet.

    Args:
        object_id: The ID of the ProductSet
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = ProductSet(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_productset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a ProductSet.

    Args:
        object_id: The ID of the ProductSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = ProductSet(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_productset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ProductSet.

    Args:
        object_id: The ID of the ProductSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ProductSet(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_productset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a ProductSet.

    Args:
        object_id: The ID of the ProductSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = ProductSet(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_automotive_models_for_productset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Automotive Models for ProductSet.

    Args:
        object_id: The ID of the ProductSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_automotive_models result
    """
    result = ProductSet(fbid=object_id).get_automotive_models(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_destinations_for_productset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Destinations for ProductSet.

    Args:
        object_id: The ID of the ProductSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_destinations result
    """
    result = ProductSet(fbid=object_id).get_destinations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_flights_for_productset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Flights for ProductSet.

    Args:
        object_id: The ID of the ProductSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_flights result
    """
    result = ProductSet(fbid=object_id).get_flights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_home_listings_for_productset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Home Listings for ProductSet.

    Args:
        object_id: The ID of the ProductSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_home_listings result
    """
    result = ProductSet(fbid=object_id).get_home_listings(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_hotels_for_productset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Hotels for ProductSet.

    Args:
        object_id: The ID of the ProductSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_hotels result
    """
    result = ProductSet(fbid=object_id).get_hotels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_media_titles_for_productset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Media Titles for ProductSet.

    Args:
        object_id: The ID of the ProductSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_media_titles result
    """
    result = ProductSet(fbid=object_id).get_media_titles(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_products_for_productset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Products for ProductSet.

    Args:
        object_id: The ID of the ProductSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_products result
    """
    result = ProductSet(fbid=object_id).get_products(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_vehicle_offers_for_productset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Vehicle Offers for ProductSet.

    Args:
        object_id: The ID of the ProductSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_vehicle_offers result
    """
    result = ProductSet(fbid=object_id).get_vehicle_offers(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_vehicles_for_productset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Vehicles for ProductSet.

    Args:
        object_id: The ID of the ProductSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_vehicles result
    """
    result = ProductSet(fbid=object_id).get_vehicles(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productset_server = mcp
