"""LiveVideoError MCP Server with typed wrappers."""

from facebook_business.adobjects.livevideoerror import LiveVideoError
from fastmcp import FastMCP

from src.generated.models.livevideoerror import LiveVideoErrorField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLiveVideoError"
instructions = """
LiveVideoError MCP Server for Facebook Business API.

Provides typed access to all LiveVideoError operations.
"""

livevideoerror_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@livevideoerror_server.tool
@wrapped_fn_tool
def get_livevideoerror(
    livevideoerror_id: str,
    fields: list[LiveVideoErrorField] = [],
) -> str:
    """Get a LiveVideoError object by ID.

    Args:
        livevideoerror_id: The ID of the LiveVideoError.
        fields: Fields to retrieve. Available fields: See LiveVideoErrorField type.
    """
    obj = LiveVideoError(livevideoerror_id)
    return obj.api_get(fields=fields)
