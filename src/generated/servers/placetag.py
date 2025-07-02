"""PlaceTag MCP Server with typed wrappers."""

from facebook_business.adobjects.placetag import PlaceTag
from fastmcp import FastMCP

from src.generated.models.placetag import PlaceTagField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPlaceTag"
instructions = """
PlaceTag MCP Server for Facebook Business API.

Provides typed access to all PlaceTag operations.
"""

placetag_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@placetag_server.tool
@wrapped_fn_tool
def get_placetag(
    placetag_id: str,
    fields: list[PlaceTagField] = [],
) -> str:
    """Get a PlaceTag object by ID.

    Args:
        placetag_id: The ID of the PlaceTag.
        fields: Fields to retrieve. Available fields: See PlaceTagField type.
    """
    obj = PlaceTag(placetag_id)
    return obj.api_get(fields=fields)
