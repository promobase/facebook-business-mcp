"""InstagramThread MCP Server."""

from typing import Any

from facebook_business.adobjects.instagramthread import InstagramThread
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookInstagramThread"
instructions = """
InstagramThread MCP Server for Facebook Business API.

Provides typed access to all InstagramThread operations.
"""

instagramthread_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@instagramthread_server.tool
@wrapped_fn_tool
def get_instagramthread(
    instagramthread_id: str,
    fields: list[str] = [],
) -> str:
    obj = InstagramThread(instagramthread_id)
    return obj.api_get(fields=fields)
