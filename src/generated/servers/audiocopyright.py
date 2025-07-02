"""AudioCopyright MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.audiocopyright import AudioCopyright
from fastmcp import FastMCP

from src.generated.models.audiocopyright import AudioCopyrightField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAudioCopyright"
instructions = """
AudioCopyright MCP Server for Facebook Business API.

Provides typed access to all AudioCopyright operations.
"""

audiocopyright_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@audiocopyright_server.tool
@wrapped_fn_tool
def get_audiocopyright(
    audiocopyright_id: str,
    fields: list[AudioCopyrightField] = [],
) -> str:
    """Get a AudioCopyright object by ID.

    Args:
        audiocopyright_id: The ID of the AudioCopyright.
        fields: Fields to retrieve. Available fields: See AudioCopyrightField type.
    """
    obj = AudioCopyright(audiocopyright_id)
    return obj.api_get(fields=fields)
