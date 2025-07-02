"""VideoTextQuestion MCP Server."""

from typing import Any

from facebook_business.adobjects.videotextquestion import VideoTextQuestion
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookVideoTextQuestion"
instructions = """
VideoTextQuestion MCP Server for Facebook Business API.

Provides typed access to all VideoTextQuestion operations.
"""

videotextquestion_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@videotextquestion_server.tool
@wrapped_fn_tool
def get_videotextquestion(
    videotextquestion_id: str,
    fields: list[str] = [],
) -> str:
    obj = VideoTextQuestion(videotextquestion_id)
    return obj.api_get(fields=fields)
