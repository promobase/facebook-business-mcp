"""AsyncSession MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.asyncsession import AsyncSession
from fastmcp import FastMCP

from src.generated.models.asyncsession import AsyncSessionField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAsyncSession"
instructions = """
AsyncSession MCP Server for Facebook Business API.

Provides typed access to all AsyncSession operations.
"""

asyncsession_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@asyncsession_server.tool
@wrapped_fn_tool
def get_asyncsession(
    asyncsession_id: str,
    fields: list[AsyncSessionField] = [],
) -> str:
    """Get a AsyncSession object by ID.

    Args:
        asyncsession_id: The ID of the AsyncSession.
        fields: Fields to retrieve. Available fields: See AsyncSessionField type.
    """
    obj = AsyncSession(asyncsession_id)
    return obj.api_get(fields=fields)
