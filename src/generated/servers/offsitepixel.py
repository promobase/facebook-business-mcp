"""OffsitePixel MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.offsitepixel import OffsitePixel
from fastmcp import FastMCP

from src.generated.models.offsitepixel import OffsitePixelField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookOffsitePixel"
instructions = """
OffsitePixel MCP Server for Facebook Business API.

Provides typed access to all OffsitePixel operations.
"""

offsitepixel_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@offsitepixel_server.tool
@wrapped_fn_tool
def get_offsitepixel(
    offsitepixel_id: str,
    fields: list[OffsitePixelField] = [],
) -> str:
    """Get a OffsitePixel object by ID.

    Args:
        offsitepixel_id: The ID of the OffsitePixel.
        fields: Fields to retrieve. Available fields: See OffsitePixelField type.
    """
    obj = OffsitePixel(offsitepixel_id)
    return obj.api_get(fields=fields)
