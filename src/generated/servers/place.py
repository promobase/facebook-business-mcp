"""Place MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.place import Place
from fastmcp import FastMCP

from src.generated.models.place import PlaceField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPlace"
instructions = """
Place MCP Server for Facebook Business API.

Provides typed access to all Place operations.
"""

place_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@place_server.tool
@wrapped_fn_tool
def get_place(
    place_id: str,
    fields: list[PlaceField] = [],
) -> str:
    """Get a Place object by ID.

    Args:
        place_id: The ID of the Place.
        fields: Fields to retrieve. Available fields: See PlaceField type.
    """
    obj = Place(place_id)
    return obj.api_get(fields=fields)
