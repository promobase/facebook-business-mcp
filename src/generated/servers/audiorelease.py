"""AudioRelease MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.audiorelease import AudioRelease
from fastmcp import FastMCP

from src.generated.models.audiorelease import AudioReleaseField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAudioRelease"
instructions = """
AudioRelease MCP Server for Facebook Business API.

Provides typed access to all AudioRelease operations.
"""

audiorelease_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@audiorelease_server.tool
@wrapped_fn_tool
def get_audiorelease(
    audiorelease_id: str,
    fields: list[AudioReleaseField] = [],
) -> str:
    """Get a AudioRelease object by ID.

    Args:
        audiorelease_id: The ID of the AudioRelease.
        fields: Fields to retrieve. Available fields: See AudioReleaseField type.
    """
    obj = AudioRelease(audiorelease_id)
    return obj.api_get(fields=fields)
