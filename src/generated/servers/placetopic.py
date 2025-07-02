"""PlaceTopic MCP Server."""

from typing import Any

from facebook_business.adobjects.placetopic import PlaceTopic
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPlaceTopic"
instructions = """
PlaceTopic MCP Server for Facebook Business API.

Provides typed access to all PlaceTopic operations.
"""

placetopic_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@placetopic_server.tool
@wrapped_fn_tool
def get_placetopic(
    placetopic_id: str,
    fields: list[str] = [],
) -> str:
    obj = PlaceTopic(placetopic_id)
    return obj.api_get(fields=fields)
