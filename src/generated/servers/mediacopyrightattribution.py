"""MediaCopyrightAttribution MCP Server."""

from typing import Any

from facebook_business.adobjects.mediacopyrightattribution import MediaCopyrightAttribution
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookMediaCopyrightAttribution"
instructions = """
MediaCopyrightAttribution MCP Server for Facebook Business API.

Provides typed access to all MediaCopyrightAttribution operations.
"""

mediacopyrightattribution_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@mediacopyrightattribution_server.tool
@wrapped_fn_tool
def get_mediacopyrightattribution(
    mediacopyrightattribution_id: str,
    fields: list[str] = [],
) -> str:
    obj = MediaCopyrightAttribution(mediacopyrightattribution_id)
    return obj.api_get(fields=fields)
