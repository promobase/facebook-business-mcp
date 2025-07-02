"""BusinessImage MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.businessimage import BusinessImage
from fastmcp import FastMCP

from src.generated.models.businessimage import BusinessImageField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessImage"
instructions = """
BusinessImage MCP Server for Facebook Business API.

Provides typed access to all BusinessImage operations.
"""

businessimage_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@businessimage_server.tool
@wrapped_fn_tool
def get_businessimage(
    businessimage_id: str,
    fields: list[BusinessImageField] = [],
) -> str:
    """Get a BusinessImage object by ID.

    Args:
        businessimage_id: The ID of the BusinessImage.
        fields: Fields to retrieve. Available fields: See BusinessImageField type.
    """
    obj = BusinessImage(businessimage_id)
    return obj.api_get(fields=fields)
