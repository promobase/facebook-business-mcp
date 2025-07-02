"""MusicWorkCopyright MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.musicworkcopyright import MusicWorkCopyright
from fastmcp import FastMCP

from src.generated.models.musicworkcopyright import MusicWorkCopyrightField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookMusicWorkCopyright"
instructions = """
MusicWorkCopyright MCP Server for Facebook Business API.

Provides typed access to all MusicWorkCopyright operations.
"""

musicworkcopyright_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@musicworkcopyright_server.tool
@wrapped_fn_tool
def get_musicworkcopyright(
    musicworkcopyright_id: str,
    fields: list[MusicWorkCopyrightField] = [],
) -> str:
    """Get a MusicWorkCopyright object by ID.

    Args:
        musicworkcopyright_id: The ID of the MusicWorkCopyright.
        fields: Fields to retrieve. Available fields: See MusicWorkCopyrightField type.
    """
    obj = MusicWorkCopyright(musicworkcopyright_id)
    return obj.api_get(fields=fields)
