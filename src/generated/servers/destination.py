"""Destination MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.destination import Destination
from fastmcp import FastMCP

from src.generated.models.destination import DestinationField, DestinationGetOverrideDetailsParams
from src.generated.models.overridedetails import OverrideDetailsField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookDestination"
instructions = """
Destination MCP Server for Facebook Business API.

Provides typed access to all Destination operations.
"""

destination_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@destination_server.tool
@wrapped_fn_tool
def get_destination(
    destination_id: str,
    fields: list[DestinationField] = [],
) -> str:
    """Get a Destination object by ID.

    Args:
        destination_id: The ID of the Destination.
        fields: Fields to retrieve. Available fields: See DestinationField type.
    """
    obj = Destination(destination_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@destination_server.tool
@wrapped_fn_tool
def get_override_details(
    destination_id: str,
    fields: list[OverrideDetailsField] = [],
    params: DestinationGetOverrideDetailsParams | dict = {},
):
    """Get Override Details for this Destination.

    Args:
        destination_id: The ID of the Destination.
        fields: Fields to retrieve. Available fields: See OverrideDetailsField type.
        params: Query parameters. Available params: See DestinationGetOverrideDetailsParams type.
    """
    return Destination(destination_id).get_override_details(fields=fields, params=params)
