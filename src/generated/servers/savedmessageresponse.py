"""SavedMessageResponse MCP Server."""

from typing import Any

from facebook_business.adobjects.savedmessageresponse import SavedMessageResponse
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = SavedMessageResponse(savedmessageresponse_id)
    return obj.api_get(fields=fields)
