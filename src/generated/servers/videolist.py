"""VideoList MCP Server."""

from typing import Any

from facebook_business.adobjects.videolist import VideoList
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookVideoList"
instructions = """
VideoList MCP Server for Facebook Business API.

Provides typed access to all VideoList operations.
"""

videolist_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@videolist_server.tool
@wrapped_fn_tool
def get_videolist(
    videolist_id: str,
    fields: list[str] = [],
) -> str:
    obj = VideoList(videolist_id)
    return obj.api_get(fields=fields)
