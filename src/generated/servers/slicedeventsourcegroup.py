"""SlicedEventSourceGroup MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.slicedeventsourcegroup import SlicedEventSourceGroup
from fastmcp import FastMCP

from src.generated.models.slicedeventsourcegroup import SlicedEventSourceGroupField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookSlicedEventSourceGroup"
instructions = """
SlicedEventSourceGroup MCP Server for Facebook Business API.

Provides typed access to all SlicedEventSourceGroup operations.
"""

slicedeventsourcegroup_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@slicedeventsourcegroup_server.tool
@wrapped_fn_tool
def get_slicedeventsourcegroup(
    slicedeventsourcegroup_id: str,
    fields: list[SlicedEventSourceGroupField] = [],
) -> str:
    """Get a SlicedEventSourceGroup object by ID.

    Args:
        slicedeventsourcegroup_id: The ID of the SlicedEventSourceGroup.
        fields: Fields to retrieve. Available fields: See SlicedEventSourceGroupField type.
    """
    obj = SlicedEventSourceGroup(slicedeventsourcegroup_id)
    return obj.api_get(fields=fields)
