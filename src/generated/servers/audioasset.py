"""AudioAsset MCP Server."""

from typing import Any

from facebook_business.adobjects.audioasset import AudioAsset
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = AudioAsset(audioasset_id)
    return obj.api_get(fields=fields)
