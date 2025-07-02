"""SavedMessageResponse MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.savedmessageresponse import SavedMessageResponse
from fastmcp import FastMCP

from src.generated.models.savedmessageresponse import SavedMessageResponseField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookSavedMessageResponse"
instructions = """
SavedMessageResponse MCP Server for Facebook Business API.

Provides typed access to all SavedMessageResponse operations.
"""

savedmessageresponse_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@savedmessageresponse_server.tool
@wrapped_fn_tool
def get_savedmessageresponse(
    savedmessageresponse_id: str,
    fields: list[SavedMessageResponseField] = [],
) -> str:
    """Get a SavedMessageResponse object by ID.

    Args:
        savedmessageresponse_id: The ID of the SavedMessageResponse.
        fields: Fields to retrieve. Available fields: See SavedMessageResponseField type.
    """
    obj = SavedMessageResponse(savedmessageresponse_id)
    return obj.api_get(fields=fields)
