"""DynamicItemDisplayBundle MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.dynamicitemdisplaybundle import DynamicItemDisplayBundle
from fastmcp import FastMCP

from src.generated.models.dynamicitemdisplaybundle import DynamicItemDisplayBundleField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookDynamicItemDisplayBundle"
instructions = """
DynamicItemDisplayBundle MCP Server for Facebook Business API.

Provides typed access to all DynamicItemDisplayBundle operations.
"""

dynamicitemdisplaybundle_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@dynamicitemdisplaybundle_server.tool
@wrapped_fn_tool
def get_dynamicitemdisplaybundle(
    dynamicitemdisplaybundle_id: str,
    fields: list[DynamicItemDisplayBundleField] = [],
) -> str:
    """Get a DynamicItemDisplayBundle object by ID.

    Args:
        dynamicitemdisplaybundle_id: The ID of the DynamicItemDisplayBundle.
        fields: Fields to retrieve. Available fields: See DynamicItemDisplayBundleField type.
    """
    obj = DynamicItemDisplayBundle(dynamicitemdisplaybundle_id)
    return obj.api_get(fields=fields)
