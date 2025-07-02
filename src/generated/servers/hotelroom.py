"""
Auto-generated MCP server for Facebook HotelRoom.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.hotelroom import HotelRoom
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-hotelroom")


# CRUD Operations


@mcp.tool()
async def get_hotelroom(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a HotelRoom.

    Args:
        object_id: The ID of the HotelRoom
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = HotelRoom(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_pricing_variables_for_hotelroom(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Pricing Variables for HotelRoom.

    Args:
        object_id: The ID of the HotelRoom
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_pricing_variables result
    """
    result = HotelRoom(fbid=object_id).get_pricing_variables(
        fields=fields,
        params=params,
    )

    return result


# Export the server
hotelroom_server = mcp
