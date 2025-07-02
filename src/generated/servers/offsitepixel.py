"""OffsitePixel MCP Server."""

from typing import Any

from facebook_business.adobjects.offsitepixel import OffsitePixel
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookOffsitePixel"
instructions = """
OffsitePixel MCP Server for Facebook Business API.

Provides typed access to all OffsitePixel operations.
"""

offsitepixel_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@offsitepixel_server.tool
@wrapped_fn_tool
def get_offsitepixel(
    offsitepixel_id: str,
    fields: list[str] = [],
) -> str:
    obj = OffsitePixel(offsitepixel_id)
    return obj.api_get(fields=fields)
