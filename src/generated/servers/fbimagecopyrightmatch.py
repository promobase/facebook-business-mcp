"""FBImageCopyrightMatch MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.fbimagecopyrightmatch import FBImageCopyrightMatch
from fastmcp import FastMCP

from src.generated.models.fbimagecopyrightmatch import FBImageCopyrightMatchField
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
    fields: list[FBImageCopyrightMatchField] = [],
) -> str:
    """Get a FBImageCopyrightMatch object by ID.

    Args:
        fbimagecopyrightmatch_id: The ID of the FBImageCopyrightMatch.
        fields: Fields to retrieve. Available fields: See FBImageCopyrightMatchField type.
    """
    obj = FBImageCopyrightMatch(fbimagecopyrightmatch_id)
    return obj.api_get(fields=fields)
