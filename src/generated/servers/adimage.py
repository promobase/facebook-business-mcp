"""AdImage MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adimage import AdImage
from fastmcp import FastMCP

from src.generated.models.adimage import AdImageField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdImage"
instructions = """
AdImage MCP Server for Facebook Business API.

Provides typed access to all AdImage operations.
"""

adimage_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adimage_server.tool
@wrapped_fn_tool
def get_adimage(
    adimage_id: str,
    fields: list[AdImageField] = [],
) -> str:
    """Get a AdImage object by ID.

    Args:
        adimage_id: The ID of the AdImage.
        fields: Fields to retrieve. Available fields: See AdImageField type.
    """
    obj = AdImage(adimage_id)
    return obj.api_get(fields=fields)
