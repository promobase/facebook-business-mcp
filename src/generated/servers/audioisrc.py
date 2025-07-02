"""AudioIsrc MCP Server."""

from typing import Any

from facebook_business.adobjects.audioisrc import AudioIsrc
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAudioIsrc"
instructions = """
AudioIsrc MCP Server for Facebook Business API.

Provides typed access to all AudioIsrc operations.
"""

audioisrc_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@audioisrc_server.tool
@wrapped_fn_tool
def get_audioisrc(
    audioisrc_id: str,
    fields: list[str] = [],
) -> str:
    obj = AudioIsrc(audioisrc_id)
    return obj.api_get(fields=fields)
