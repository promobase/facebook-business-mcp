"""PageBroadcast MCP Server."""

from typing import Any

from facebook_business.adobjects.pagebroadcast import PageBroadcast
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPageBroadcast"
instructions = """
PageBroadcast MCP Server for Facebook Business API.

Provides typed access to all PageBroadcast operations.
"""

pagebroadcast_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@pagebroadcast_server.tool
@wrapped_fn_tool
def get_pagebroadcast(
    pagebroadcast_id: str,
    fields: list[str] = [],
) -> str:
    obj = PageBroadcast(pagebroadcast_id)
    return obj.api_get(fields=fields)
