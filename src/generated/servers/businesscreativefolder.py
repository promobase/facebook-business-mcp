"""BusinessCreativeFolder MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.businesscreativefolder import BusinessCreativeFolder
from fastmcp import FastMCP

from src.generated.models.businesscreativefolder import BusinessCreativeFolderField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessCreativeFolder"
instructions = """
BusinessCreativeFolder MCP Server for Facebook Business API.

Provides typed access to all BusinessCreativeFolder operations.
"""

businesscreativefolder_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@businesscreativefolder_server.tool
@wrapped_fn_tool
def get_businesscreativefolder(
    businesscreativefolder_id: str,
    fields: list[BusinessCreativeFolderField] = [],
) -> str:
    """Get a BusinessCreativeFolder object by ID.

    Args:
        businesscreativefolder_id: The ID of the BusinessCreativeFolder.
        fields: Fields to retrieve. Available fields: See BusinessCreativeFolderField type.
    """
    obj = BusinessCreativeFolder(businesscreativefolder_id)
    return obj.api_get(fields=fields)
