"""FBImageCopyrightMatch MCP Server."""

from typing import Any

from facebook_business.adobjects.fbimagecopyrightmatch import FBImageCopyrightMatch
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookFBImageCopyrightMatch"
instructions = """
FBImageCopyrightMatch MCP Server for Facebook Business API.

Provides typed access to all FBImageCopyrightMatch operations.
"""

fbimagecopyrightmatch_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@fbimagecopyrightmatch_server.tool
@wrapped_fn_tool
def get_fbimagecopyrightmatch(
    fbimagecopyrightmatch_id: str,
    fields: list[str] = [],
) -> str:
    obj = FBImageCopyrightMatch(fbimagecopyrightmatch_id)
    return obj.api_get(fields=fields)
