"""Vehicle MCP Server."""

from typing import Any

from facebook_business.adobjects.vehicle import Vehicle
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookVehicle"
instructions = """
Vehicle MCP Server for Facebook Business API.

Provides typed access to all Vehicle operations.
"""

vehicle_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@vehicle_server.tool
@wrapped_fn_tool
def get_vehicle(
    vehicle_id: str,
    fields: list[str] = [],
) -> str:
    obj = Vehicle(vehicle_id)
    return obj.api_get(fields=fields)


@vehicle_server.tool
@wrapped_fn_tool
def update_vehicle(
    vehicle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Vehicle(vehicle_id).api_update(fields=fields, params=params)


# ---- Edge Methods (3) ----
@vehicle_server.tool
@wrapped_fn_tool
def get_channels_to_integrity_status(
    vehicle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Vehicle(vehicle_id).get_channels_to_integrity_status(fields=fields, params=params)


@vehicle_server.tool
@wrapped_fn_tool
def get_override_details(
    vehicle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Vehicle(vehicle_id).get_override_details(fields=fields, params=params)


@vehicle_server.tool
@wrapped_fn_tool
def get_videos_metadata(
    vehicle_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Vehicle(vehicle_id).get_videos_metadata(fields=fields, params=params)
