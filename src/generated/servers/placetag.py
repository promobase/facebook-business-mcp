"""PlaceTag MCP Server."""

from typing import Any

from facebook_business.adobjects.placetag import PlaceTag
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPlaceTag"
instructions = """
PlaceTag MCP Server for Facebook Business API.

Provides typed access to all PlaceTag operations.
"""

placetag_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@placetag_server.tool
@wrapped_fn_tool
def get_placetag(
    placetag_id: str,
    fields: list[str] = [],
) -> str:
    obj = PlaceTag(placetag_id)
    return obj.api_get(fields=fields)
