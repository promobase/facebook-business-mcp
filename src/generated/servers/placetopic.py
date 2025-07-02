"""PlaceTopic MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.placetopic import PlaceTopic
from fastmcp import FastMCP

from src.generated.models.placetopic import PlaceTopicField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPlaceTopic"
instructions = """
PlaceTopic MCP Server for Facebook Business API.

Provides typed access to all PlaceTopic operations.
"""

placetopic_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@placetopic_server.tool
@wrapped_fn_tool
def get_placetopic(
    placetopic_id: str,
    fields: list[PlaceTopicField] = [],
) -> str:
    """Get a PlaceTopic object by ID.

    Args:
        placetopic_id: The ID of the PlaceTopic.
        fields: Fields to retrieve. Available fields: See PlaceTopicField type.
    """
    obj = PlaceTopic(placetopic_id)
    return obj.api_get(fields=fields)
