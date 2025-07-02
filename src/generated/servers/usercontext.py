"""UserContext MCP Server."""

from typing import Any

from facebook_business.adobjects.usercontext import UserContext
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = UserContext(usercontext_id)
    return obj.api_get(fields=fields)
