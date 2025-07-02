"""AdPlacement MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adplacement import AdPlacement
from fastmcp import FastMCP

from src.generated.models.adplacement import AdPlacementField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdPlacement"
instructions = """
AdPlacement MCP Server for Facebook Business API.

Provides typed access to all AdPlacement operations.
"""

adplacement_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adplacement_server.tool
@wrapped_fn_tool
def get_adplacement(
    adplacement_id: str,
    fields: list[AdPlacementField] = [],
) -> str:
    """Get a AdPlacement object by ID.

    Args:
        adplacement_id: The ID of the AdPlacement.
        fields: Fields to retrieve. Available fields: See AdPlacementField type.
    """
    obj = AdPlacement(adplacement_id)
    return obj.api_get(fields=fields)
