"""Flight MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.flight import Flight
from fastmcp import FastMCP

from src.generated.models.flight import (
    FlightField,
    FlightGetOverrideDetailsParams,
    FlightUpdateParams,
)
from src.generated.models.overridedetails import OverrideDetailsField
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
    fields: list[FlightField] = [],
) -> str:
    """Get a Flight object by ID.

    Args:
        flight_id: The ID of the Flight.
        fields: Fields to retrieve. Available fields: See FlightField type.
    """
    obj = Flight(flight_id)
    return obj.api_get(fields=fields)


@flight_server.tool
@wrapped_fn_tool
def update_flight(
    flight_id: str,
    fields: list[FlightField] = [],
    params: FlightUpdateParams | dict = {},
) -> str:
    """Update a Flight object.

    Args:
        flight_id: The ID of the Flight.
        fields: Fields to return after update. Available fields: See FlightField type.
        params: Parameters to update. Available params: See FlightUpdateParams type.
    """
    return Flight(flight_id).api_update(fields=fields, params=params)


# ---- Edge Methods (1) ----
@flight_server.tool
@wrapped_fn_tool
def get_override_details(
    flight_id: str,
    fields: list[OverrideDetailsField] = [],
    params: FlightGetOverrideDetailsParams | dict = {},
):
    """Get Override Details for this Flight.

    Args:
        flight_id: The ID of the Flight.
        fields: Fields to retrieve. Available fields: See OverrideDetailsField type.
        params: Query parameters. Available params: See FlightGetOverrideDetailsParams type.
    """
    return Flight(flight_id).get_override_details(fields=fields, params=params)
