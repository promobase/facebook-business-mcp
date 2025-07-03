"""
Auto-generated MCP server for Facebook Hotel.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.hotel import Hotel
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-hotel")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    hotel_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Hotel(fbid=hotel_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    hotel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Hotel(fbid=hotel_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    hotel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Hotel(fbid=hotel_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    hotel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Hotel(fbid=hotel_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_channels_to_integrity_status(
    hotel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Hotel(fbid=hotel_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_hotel_rooms(
    hotel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Hotel(fbid=hotel_id).get_hotel_rooms(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_override_details(
    hotel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Hotel(fbid=hotel_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_videos_metadata(
    hotel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Hotel(fbid=hotel_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
hotel_server = mcp
