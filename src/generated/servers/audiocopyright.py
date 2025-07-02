"""AudioCopyright MCP Server."""

from typing import Any

from facebook_business.adobjects.audiocopyright import AudioCopyright
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = AudioCopyright(audiocopyright_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@audiocopyright_server.tool
@wrapped_fn_tool
def get_update_records(
    audiocopyright_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AudioCopyright(audiocopyright_id).get_update_records(fields=fields, params=params)
