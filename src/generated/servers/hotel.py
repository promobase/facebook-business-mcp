"""Hotel MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.hotel import Hotel
from fastmcp import FastMCP

from src.generated.models.hotel import HotelField, HotelGetOverrideDetailsParams, HotelUpdateParams
from src.generated.models.overridedetails import OverrideDetailsField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookHotel"
instructions = """
Hotel MCP Server for Facebook Business API.

Provides typed access to all Hotel operations.
"""

hotel_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@hotel_server.tool
@wrapped_fn_tool
def get_hotel(
    hotel_id: str,
    fields: list[HotelField] = [],
) -> str:
    """Get a Hotel object by ID.

    Args:
        hotel_id: The ID of the Hotel.
        fields: Fields to retrieve. Available fields: See HotelField type.
    """
    obj = Hotel(hotel_id)
    return obj.api_get(fields=fields)


@hotel_server.tool
@wrapped_fn_tool
def update_hotel(
    hotel_id: str,
    fields: list[HotelField] = [],
    params: HotelUpdateParams | dict = {},
) -> str:
    """Update a Hotel object.

    Args:
        hotel_id: The ID of the Hotel.
        fields: Fields to return after update. Available fields: See HotelField type.
        params: Parameters to update. Available params: See HotelUpdateParams type.
    """
    return Hotel(hotel_id).api_update(fields=fields, params=params)


@hotel_server.tool
@wrapped_fn_tool
def delete_hotel(
    hotel_id: str,
) -> str:
    """Delete a Hotel object.

    Args:
        hotel_id: The ID of the Hotel.
    """
    return Hotel(hotel_id).api_delete()


# ---- Edge Methods (1) ----
@hotel_server.tool
@wrapped_fn_tool
def get_override_details(
    hotel_id: str,
    fields: list[OverrideDetailsField] = [],
    params: HotelGetOverrideDetailsParams | dict = {},
):
    """Get Override Details for this Hotel.

    Args:
        hotel_id: The ID of the Hotel.
        fields: Fields to retrieve. Available fields: See OverrideDetailsField type.
        params: Query parameters. Available params: See HotelGetOverrideDetailsParams type.
    """
    return Hotel(hotel_id).get_override_details(fields=fields, params=params)
