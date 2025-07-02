"""Flight MCP Server."""

from typing import Any

from facebook_business.adobjects.flight import Flight
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookFlight"
instructions = """
Flight MCP Server for Facebook Business API.

Provides typed access to all Flight operations.
"""

flight_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@flight_server.tool
@wrapped_fn_tool
def get_flight(
    flight_id: str,
    fields: list[str] = [],
) -> str:
    obj = Flight(flight_id)
    return obj.api_get(fields=fields)


@flight_server.tool
@wrapped_fn_tool
def update_flight(
    flight_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Flight(flight_id).api_update(fields=fields, params=params)


# ---- Edge Methods (3) ----
@flight_server.tool
@wrapped_fn_tool
def get_channels_to_integrity_status(
    flight_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Flight(flight_id).get_channels_to_integrity_status(fields=fields, params=params)


@flight_server.tool
@wrapped_fn_tool
def get_override_details(
    flight_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Flight(flight_id).get_override_details(fields=fields, params=params)


@flight_server.tool
@wrapped_fn_tool
def get_videos_metadata(
    flight_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Flight(flight_id).get_videos_metadata(fields=fields, params=params)
