"""StoreLocation MCP Server."""

from typing import Any

from facebook_business.adobjects.storelocation import StoreLocation
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookStoreLocation"
instructions = """
StoreLocation MCP Server for Facebook Business API.

Provides typed access to all StoreLocation operations.
"""

storelocation_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@storelocation_server.tool
@wrapped_fn_tool
def get_storelocation(
    storelocation_id: str,
    fields: list[str] = [],
) -> str:
    obj = StoreLocation(storelocation_id)
    return obj.api_get(fields=fields)
