"""UnifiedThread MCP Server."""

from typing import Any

from facebook_business.adobjects.unifiedthread import UnifiedThread
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookUnifiedThread"
instructions = """
UnifiedThread MCP Server for Facebook Business API.

Provides typed access to all UnifiedThread operations.
"""

unifiedthread_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@unifiedthread_server.tool
@wrapped_fn_tool
def get_unifiedthread(
    unifiedthread_id: str,
    fields: list[str] = [],
) -> str:
    obj = UnifiedThread(unifiedthread_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@unifiedthread_server.tool
@wrapped_fn_tool
def get_messages(
    unifiedthread_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return UnifiedThread(unifiedthread_id).get_messages(fields=fields, params=params)
