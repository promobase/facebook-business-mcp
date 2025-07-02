"""MusicVideoCopyright MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.musicvideocopyright import MusicVideoCopyright
from fastmcp import FastMCP

from src.generated.models.musicvideocopyright import MusicVideoCopyrightField
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
    fields: list[MusicVideoCopyrightField] = [],
) -> str:
    """Get a MusicVideoCopyright object by ID.

    Args:
        musicvideocopyright_id: The ID of the MusicVideoCopyright.
        fields: Fields to retrieve. Available fields: See MusicVideoCopyrightField type.
    """
    obj = MusicVideoCopyright(musicvideocopyright_id)
    return obj.api_get(fields=fields)
