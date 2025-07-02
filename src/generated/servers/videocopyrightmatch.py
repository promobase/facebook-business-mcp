"""VideoCopyrightMatch MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.videocopyrightmatch import VideoCopyrightMatch
from fastmcp import FastMCP

from src.generated.models.videocopyrightmatch import VideoCopyrightMatchField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookVideoCopyrightMatch"
instructions = """
VideoCopyrightMatch MCP Server for Facebook Business API.

Provides typed access to all VideoCopyrightMatch operations.
"""

videocopyrightmatch_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@videocopyrightmatch_server.tool
@wrapped_fn_tool
def get_videocopyrightmatch(
    videocopyrightmatch_id: str,
    fields: list[VideoCopyrightMatchField] = [],
) -> str:
    """Get a VideoCopyrightMatch object by ID.

    Args:
        videocopyrightmatch_id: The ID of the VideoCopyrightMatch.
        fields: Fields to retrieve. Available fields: See VideoCopyrightMatchField type.
    """
    obj = VideoCopyrightMatch(videocopyrightmatch_id)
    return obj.api_get(fields=fields)
