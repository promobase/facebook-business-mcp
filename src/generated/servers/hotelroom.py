"""HotelRoom MCP Server with typed wrappers."""

from facebook_business.adobjects.hotelroom import HotelRoom
from fastmcp import FastMCP

from src.generated.models.hotelroom import HotelRoomField
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
    fields: list[HotelRoomField] = [],
) -> str:
    """Get a HotelRoom object by ID.

    Args:
        hotelroom_id: The ID of the HotelRoom.
        fields: Fields to retrieve. Available fields: See HotelRoomField type.
    """
    obj = HotelRoom(hotelroom_id)
    return obj.api_get(fields=fields)
