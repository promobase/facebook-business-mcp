"""VehicleOffer MCP Server with typed wrappers."""

from facebook_business.adobjects.vehicleoffer import VehicleOffer
from fastmcp import FastMCP

from src.generated.models.overridedetails import OverrideDetailsField
from src.generated.models.vehicleoffer import (
    VehicleOfferField,
    VehicleOfferGetOverrideDetailsParams,
)
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
    fields: list[VehicleOfferField] = [],
) -> str:
    """Get a VehicleOffer object by ID.

    Args:
        vehicleoffer_id: The ID of the VehicleOffer.
        fields: Fields to retrieve. Available fields: See VehicleOfferField type.
    """
    obj = VehicleOffer(vehicleoffer_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@vehicleoffer_server.tool
@wrapped_fn_tool
def get_override_details(
    vehicleoffer_id: str,
    fields: list[OverrideDetailsField] = [],
    params: VehicleOfferGetOverrideDetailsParams | dict = {},
):
    """Get Override Details for this VehicleOffer.

    Args:
        vehicleoffer_id: The ID of the VehicleOffer.
        fields: Fields to retrieve. Available fields: See OverrideDetailsField type.
        params: Query parameters. Available params: See VehicleOfferGetOverrideDetailsParams type.
    """
    return VehicleOffer(vehicleoffer_id).get_override_details(fields=fields, params=params)
