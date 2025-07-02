"""CreatorAssetCreative MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.creatorassetcreative import CreatorAssetCreative
from fastmcp import FastMCP

from src.generated.models.creatorassetcreative import CreatorAssetCreativeField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCreatorAssetCreative"
instructions = """
CreatorAssetCreative MCP Server for Facebook Business API.

Provides typed access to all CreatorAssetCreative operations.
"""

creatorassetcreative_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@creatorassetcreative_server.tool
@wrapped_fn_tool
def get_creatorassetcreative(
    creatorassetcreative_id: str,
    fields: list[CreatorAssetCreativeField] = [],
) -> str:
    """Get a CreatorAssetCreative object by ID.

    Args:
        creatorassetcreative_id: The ID of the CreatorAssetCreative.
        fields: Fields to retrieve. Available fields: See CreatorAssetCreativeField type.
    """
    obj = CreatorAssetCreative(creatorassetcreative_id)
    return obj.api_get(fields=fields)
