"""ImageCopyrightDispute MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.imagecopyrightdispute import ImageCopyrightDispute
from fastmcp import FastMCP

from src.generated.models.imagecopyrightdispute import ImageCopyrightDisputeField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookImageCopyrightDispute"
instructions = """
ImageCopyrightDispute MCP Server for Facebook Business API.

Provides typed access to all ImageCopyrightDispute operations.
"""

imagecopyrightdispute_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@imagecopyrightdispute_server.tool
@wrapped_fn_tool
def get_imagecopyrightdispute(
    imagecopyrightdispute_id: str,
    fields: list[ImageCopyrightDisputeField] = [],
) -> str:
    """Get a ImageCopyrightDispute object by ID.

    Args:
        imagecopyrightdispute_id: The ID of the ImageCopyrightDispute.
        fields: Fields to retrieve. Available fields: See ImageCopyrightDisputeField type.
    """
    obj = ImageCopyrightDispute(imagecopyrightdispute_id)
    return obj.api_get(fields=fields)
