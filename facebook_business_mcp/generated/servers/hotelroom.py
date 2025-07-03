"""
Auto-generated MCP server for Facebook HotelRoom.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.hotelroom import HotelRoom
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-hotelroom")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    hotelroom_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = HotelRoom(fbid=hotelroom_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    hotelroom_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = HotelRoom(fbid=hotelroom_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    hotelroom_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = HotelRoom(fbid=hotelroom_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    hotelroom_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = HotelRoom(fbid=hotelroom_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_pricing_variables(
    hotelroom_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = HotelRoom(fbid=hotelroom_id).get_pricing_variables(
        fields=fields,
        params=params,
    )

    return result


# Export the server
hotelroom_server = mcp
