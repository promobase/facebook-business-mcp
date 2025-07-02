"""PlayableContent MCP Server."""

from typing import Any

from facebook_business.adobjects.playablecontent import PlayableContent
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPlayableContent"
instructions = """
PlayableContent MCP Server for Facebook Business API.

Provides typed access to all PlayableContent operations.
"""

playablecontent_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@playablecontent_server.tool
@wrapped_fn_tool
def get_playablecontent(
    playablecontent_id: str,
    fields: list[str] = [],
) -> str:
    obj = PlayableContent(playablecontent_id)
    return obj.api_get(fields=fields)
