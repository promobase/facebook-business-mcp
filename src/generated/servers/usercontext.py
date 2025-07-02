"""UserContext MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.usercontext import UserContext
from fastmcp import FastMCP

from src.generated.models.usercontext import UserContextField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookUserContext"
instructions = """
UserContext MCP Server for Facebook Business API.

Provides typed access to all UserContext operations.
"""

usercontext_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@usercontext_server.tool
@wrapped_fn_tool
def get_usercontext(
    usercontext_id: str,
    fields: list[UserContextField] = [],
) -> str:
    """Get a UserContext object by ID.

    Args:
        usercontext_id: The ID of the UserContext.
        fields: Fields to retrieve. Available fields: See UserContextField type.
    """
    obj = UserContext(usercontext_id)
    return obj.api_get(fields=fields)
