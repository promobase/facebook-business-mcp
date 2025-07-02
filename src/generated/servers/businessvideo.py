"""BusinessVideo MCP Server with typed wrappers."""

from facebook_business.adobjects.businessvideo import BusinessVideo
from fastmcp import FastMCP

from src.generated.models.businessvideo import BusinessVideoField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessVideo"
instructions = """
BusinessVideo MCP Server for Facebook Business API.

Provides typed access to all BusinessVideo operations.
"""

businessvideo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@businessvideo_server.tool
@wrapped_fn_tool
def get_businessvideo(
    businessvideo_id: str,
    fields: list[BusinessVideoField] = [],
) -> str:
    """Get a BusinessVideo object by ID.

    Args:
        businessvideo_id: The ID of the BusinessVideo.
        fields: Fields to retrieve. Available fields: See BusinessVideoField type.
    """
    obj = BusinessVideo(businessvideo_id)
    return obj.api_get(fields=fields)
