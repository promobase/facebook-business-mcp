"""HotelRoom MCP Server."""

from typing import Any

from facebook_business.adobjects.hotelroom import HotelRoom
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookHotelRoom"
instructions = """
HotelRoom MCP Server for Facebook Business API.

Provides typed access to all HotelRoom operations.
"""

hotelroom_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@hotelroom_server.tool
@wrapped_fn_tool
def get_hotelroom(
    hotelroom_id: str,
    fields: list[str] = [],
) -> str:
    obj = HotelRoom(hotelroom_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@hotelroom_server.tool
@wrapped_fn_tool
def get_pricing_variables(
    hotelroom_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return HotelRoom(hotelroom_id).get_pricing_variables(fields=fields, params=params)
