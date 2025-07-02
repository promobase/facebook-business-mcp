"""MusicVideoCopyright MCP Server."""

from typing import Any

from facebook_business.adobjects.musicvideocopyright import MusicVideoCopyright
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookMusicVideoCopyright"
instructions = """
MusicVideoCopyright MCP Server for Facebook Business API.

Provides typed access to all MusicVideoCopyright operations.
"""

musicvideocopyright_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@musicvideocopyright_server.tool
@wrapped_fn_tool
def get_musicvideocopyright(
    musicvideocopyright_id: str,
    fields: list[str] = [],
) -> str:
    obj = MusicVideoCopyright(musicvideocopyright_id)
    return obj.api_get(fields=fields)
