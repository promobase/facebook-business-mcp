"""
Auto-generated MCP server for Facebook ProductSet.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productset import ProductSet
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
    result = ProductSet(fbid=object_id).get_vehicles(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productset_server = mcp
