"""DynamicContentSet MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.dynamiccontentset import DynamicContentSet
from fastmcp import FastMCP

from src.generated.models.dynamiccontentset import DynamicContentSetField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookDynamicContentSet"
instructions = """
DynamicContentSet MCP Server for Facebook Business API.

Provides typed access to all DynamicContentSet operations.
"""

dynamiccontentset_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@dynamiccontentset_server.tool
@wrapped_fn_tool
def get_dynamiccontentset(
    dynamiccontentset_id: str,
    fields: list[DynamicContentSetField] = [],
) -> str:
    """Get a DynamicContentSet object by ID.

    Args:
        dynamiccontentset_id: The ID of the DynamicContentSet.
        fields: Fields to retrieve. Available fields: See DynamicContentSetField type.
    """
    obj = DynamicContentSet(dynamiccontentset_id)
    return obj.api_get(fields=fields)
