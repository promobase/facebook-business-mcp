"""Vehicle MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.vehicle import Vehicle
from fastmcp import FastMCP

from src.generated.models.overridedetails import OverrideDetailsField
from src.generated.models.vehicle import (
    VehicleField,
    VehicleGetOverrideDetailsParams,
    VehicleUpdateParams,
)
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
    fields: list[VehicleField] = [],
) -> str:
    """Get a Vehicle object by ID.

    Args:
        vehicle_id: The ID of the Vehicle.
        fields: Fields to retrieve. Available fields: See VehicleField type.
    """
    obj = Vehicle(vehicle_id)
    return obj.api_get(fields=fields)


@vehicle_server.tool
@wrapped_fn_tool
def update_vehicle(
    vehicle_id: str,
    fields: list[VehicleField] = [],
    params: VehicleUpdateParams | dict = {},
) -> str:
    """Update a Vehicle object.

    Args:
        vehicle_id: The ID of the Vehicle.
        fields: Fields to return after update. Available fields: See VehicleField type.
        params: Parameters to update. Available params: See VehicleUpdateParams type.
    """
    return Vehicle(vehicle_id).api_update(fields=fields, params=params)


# ---- Edge Methods (1) ----
@vehicle_server.tool
@wrapped_fn_tool
def get_override_details(
    vehicle_id: str,
    fields: list[OverrideDetailsField] = [],
    params: VehicleGetOverrideDetailsParams | dict = {},
):
    """Get Override Details for this Vehicle.

    Args:
        vehicle_id: The ID of the Vehicle.
        fields: Fields to retrieve. Available fields: See OverrideDetailsField type.
        params: Query parameters. Available params: See VehicleGetOverrideDetailsParams type.
    """
    return Vehicle(vehicle_id).get_override_details(fields=fields, params=params)
