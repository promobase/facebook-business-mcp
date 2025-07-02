"""AudioAsset MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.audioasset import AudioAsset
from fastmcp import FastMCP

from src.generated.models.audioasset import AudioAssetField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAudioAsset"
instructions = """
AudioAsset MCP Server for Facebook Business API.

Provides typed access to all AudioAsset operations.
"""

audioasset_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@audioasset_server.tool
@wrapped_fn_tool
def get_audioasset(
    audioasset_id: str,
    fields: list[AudioAssetField] = [],
) -> str:
    """Get a AudioAsset object by ID.

    Args:
        audioasset_id: The ID of the AudioAsset.
        fields: Fields to retrieve. Available fields: See AudioAssetField type.
    """
    obj = AudioAsset(audioasset_id)
    return obj.api_get(fields=fields)
