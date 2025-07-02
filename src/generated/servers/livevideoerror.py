"""LiveVideoError MCP Server."""

from typing import Any

from facebook_business.adobjects.livevideoerror import LiveVideoError
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = LiveVideoError(livevideoerror_id)
    return obj.api_get(fields=fields)
