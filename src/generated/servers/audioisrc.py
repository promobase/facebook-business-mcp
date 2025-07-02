"""AudioIsrc MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.audioisrc import AudioIsrc
from fastmcp import FastMCP

from src.generated.models.audioisrc import AudioIsrcField
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
    fields: list[AudioIsrcField] = [],
) -> str:
    """Get a AudioIsrc object by ID.

    Args:
        audioisrc_id: The ID of the AudioIsrc.
        fields: Fields to retrieve. Available fields: See AudioIsrcField type.
    """
    obj = AudioIsrc(audioisrc_id)
    return obj.api_get(fields=fields)
