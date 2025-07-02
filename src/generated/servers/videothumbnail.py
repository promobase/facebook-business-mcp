"""VideoThumbnail MCP Server."""

from typing import Any

from facebook_business.adobjects.videothumbnail import VideoThumbnail
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookVideoThumbnail"
instructions = """
VideoThumbnail MCP Server for Facebook Business API.

Provides typed access to all VideoThumbnail operations.
"""

videothumbnail_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@videothumbnail_server.tool
@wrapped_fn_tool
def get_endpoint(
    videothumbnail_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return VideoThumbnail(videothumbnail_id).get_endpoint(fields=fields, params=params)
