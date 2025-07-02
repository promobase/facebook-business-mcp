"""
Auto-generated MCP server for Facebook Flight.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.flight import Flight
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-flight")


# CRUD Operations


@mcp.tool()
async def api_create_flight(
    flight_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Flight(fbid=flight_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_flight(
    flight_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Flight(fbid=flight_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_flight(
    flight_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Flight(fbid=flight_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_flight(
    flight_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Flight(fbid=flight_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_channels_to_integrity_status(
    flight_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Flight(fbid=flight_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_override_details(
    flight_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Flight(fbid=flight_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_videos_metadata(
    flight_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Flight(fbid=flight_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
flight_server = mcp
