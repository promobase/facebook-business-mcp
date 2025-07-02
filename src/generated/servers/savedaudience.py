"""SavedAudience MCP Server."""

from typing import Any

from facebook_business.adobjects.savedaudience import SavedAudience
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookSavedAudience"
instructions = """
SavedAudience MCP Server for Facebook Business API.

Provides typed access to all SavedAudience operations.
"""

savedaudience_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@savedaudience_server.tool
@wrapped_fn_tool
def get_savedaudience(
    savedaudience_id: str,
    fields: list[str] = [],
) -> str:
    obj = SavedAudience(savedaudience_id)
    return obj.api_get(fields=fields)
