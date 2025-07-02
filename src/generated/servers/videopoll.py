"""VideoPoll MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.videopoll import VideoPoll
from fastmcp import FastMCP

from src.generated.models.videopoll import VideoPollField, VideoPollUpdateParams
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookVideoPoll"
instructions = """
VideoPoll MCP Server for Facebook Business API.

Provides typed access to all VideoPoll operations.
"""

videopoll_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@videopoll_server.tool
@wrapped_fn_tool
def get_videopoll(
    videopoll_id: str,
    fields: list[VideoPollField] = [],
) -> str:
    """Get a VideoPoll object by ID.

    Args:
        videopoll_id: The ID of the VideoPoll.
        fields: Fields to retrieve. Available fields: See VideoPollField type.
    """
    obj = VideoPoll(videopoll_id)
    return obj.api_get(fields=fields)


@videopoll_server.tool
@wrapped_fn_tool
def update_videopoll(
    videopoll_id: str,
    fields: list[VideoPollField] = [],
    params: VideoPollUpdateParams | dict = {},
) -> str:
    """Update a VideoPoll object.

    Args:
        videopoll_id: The ID of the VideoPoll.
        fields: Fields to return after update. Available fields: See VideoPollField type.
        params: Parameters to update. Available params: See VideoPollUpdateParams type.
    """
    return VideoPoll(videopoll_id).api_update(fields=fields, params=params)
