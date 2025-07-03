"""
Auto-generated MCP server for Facebook Flight.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.flight import Flight
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-flight")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    flight_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Flight(fbid=flight_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    flight_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Flight(fbid=flight_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    flight_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Flight(fbid=flight_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    flight_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Flight(fbid=flight_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_channels_to_integrity_status(
    flight_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Flight(fbid=flight_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_override_details(
    flight_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Flight(fbid=flight_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_videos_metadata(
    flight_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Flight(fbid=flight_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
flight_server = mcp
