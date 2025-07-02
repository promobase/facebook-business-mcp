"""VehicleOffer MCP Server."""

from typing import Any

from facebook_business.adobjects.vehicleoffer import VehicleOffer
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookVehicleOffer"
instructions = """
VehicleOffer MCP Server for Facebook Business API.

Provides typed access to all VehicleOffer operations.
"""

vehicleoffer_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@vehicleoffer_server.tool
@wrapped_fn_tool
def get_vehicleoffer(
    vehicleoffer_id: str,
    fields: list[str] = [],
) -> str:
    obj = VehicleOffer(vehicleoffer_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (3) ----
@vehicleoffer_server.tool
@wrapped_fn_tool
def get_channels_to_integrity_status(
    vehicleoffer_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return VehicleOffer(vehicleoffer_id).get_channels_to_integrity_status(
        fields=fields, params=params
    )


@vehicleoffer_server.tool
@wrapped_fn_tool
def get_override_details(
    vehicleoffer_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return VehicleOffer(vehicleoffer_id).get_override_details(fields=fields, params=params)


@vehicleoffer_server.tool
@wrapped_fn_tool
def get_videos_metadata(
    vehicleoffer_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return VehicleOffer(vehicleoffer_id).get_videos_metadata(fields=fields, params=params)
