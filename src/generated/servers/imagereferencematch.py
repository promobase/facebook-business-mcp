"""ImageReferenceMatch MCP Server with typed wrappers."""

from facebook_business.adobjects.imagereferencematch import ImageReferenceMatch
from fastmcp import FastMCP

from src.generated.models.imagereferencematch import ImageReferenceMatchField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookImageReferenceMatch"
instructions = """
ImageReferenceMatch MCP Server for Facebook Business API.

Provides typed access to all ImageReferenceMatch operations.
"""

imagereferencematch_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@imagereferencematch_server.tool
@wrapped_fn_tool
def get_imagereferencematch(
    imagereferencematch_id: str,
    fields: list[ImageReferenceMatchField] = [],
) -> str:
    """Get a ImageReferenceMatch object by ID.

    Args:
        imagereferencematch_id: The ID of the ImageReferenceMatch.
        fields: Fields to retrieve. Available fields: See ImageReferenceMatchField type.
    """
    obj = ImageReferenceMatch(imagereferencematch_id)
    return obj.api_get(fields=fields)
