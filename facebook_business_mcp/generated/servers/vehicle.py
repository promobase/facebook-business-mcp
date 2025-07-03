"""
Auto-generated MCP server for Facebook Vehicle.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.vehicle import Vehicle
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-vehicle")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    vehicle_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Vehicle(fbid=vehicle_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    vehicle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Vehicle(fbid=vehicle_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    vehicle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Vehicle(fbid=vehicle_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    vehicle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Vehicle(fbid=vehicle_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_channels_to_integrity_status(
    vehicle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Vehicle(fbid=vehicle_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_override_details(
    vehicle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Vehicle(fbid=vehicle_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_videos_metadata(
    vehicle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Vehicle(fbid=vehicle_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
vehicle_server = mcp
