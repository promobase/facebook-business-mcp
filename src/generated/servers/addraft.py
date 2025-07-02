"""AdDraft MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.addraft import AdDraft
from fastmcp import FastMCP

from src.generated.models.addraft import AdDraftField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdDraft"
instructions = """
AdDraft MCP Server for Facebook Business API.

Provides typed access to all AdDraft operations.
"""

addraft_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@addraft_server.tool
@wrapped_fn_tool
def get_addraft(
    addraft_id: str,
    fields: list[AdDraftField] = [],
) -> str:
    """Get a AdDraft object by ID.

    Args:
        addraft_id: The ID of the AdDraft.
        fields: Fields to retrieve. Available fields: See AdDraftField type.
    """
    obj = AdDraft(addraft_id)
    return obj.api_get(fields=fields)
