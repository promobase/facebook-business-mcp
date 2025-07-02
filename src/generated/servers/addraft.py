"""AdDraft MCP Server."""

from typing import Any

from facebook_business.adobjects.addraft import AdDraft
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = AdDraft(addraft_id)
    return obj.api_get(fields=fields)
