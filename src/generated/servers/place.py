"""Place MCP Server."""

from typing import Any

from facebook_business.adobjects.place import Place
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPlace"
instructions = """
Place MCP Server for Facebook Business API.

Provides typed access to all Place operations.
"""

place_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@place_server.tool
@wrapped_fn_tool
def get_place(
    place_id: str,
    fields: list[str] = [],
) -> str:
    obj = Place(place_id)
    return obj.api_get(fields=fields)
