"""Hotel MCP Server."""

from typing import Any

from facebook_business.adobjects.hotel import Hotel
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = Hotel(hotel_id)
    return obj.api_get(fields=fields)


@hotel_server.tool
@wrapped_fn_tool
def update_hotel(
    hotel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Hotel(hotel_id).api_update(fields=fields, params=params)


@hotel_server.tool
@wrapped_fn_tool
def delete_hotel(
    hotel_id: str,
) -> str:
    return Hotel(hotel_id).api_delete()


# ---- Edge Methods (1) ----
@hotel_server.tool
@wrapped_fn_tool
def get_override_details(
    hotel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Hotel(hotel_id).get_override_details(fields=fields, params=params)
