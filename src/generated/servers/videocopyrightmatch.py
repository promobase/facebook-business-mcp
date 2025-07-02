"""VideoCopyrightMatch MCP Server."""

from typing import Any

from facebook_business.adobjects.videocopyrightmatch import VideoCopyrightMatch
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = VideoCopyrightMatch(videocopyrightmatch_id)
    return obj.api_get(fields=fields)
