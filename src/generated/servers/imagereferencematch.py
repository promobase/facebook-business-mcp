"""ImageReferenceMatch MCP Server."""

from typing import Any

from facebook_business.adobjects.imagereferencematch import ImageReferenceMatch
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookImageReferenceMatch"
instructions = """
ImageReferenceMatch MCP Server for Facebook Business API.

Provides typed access to all ImageReferenceMatch operations.
"""

imagereferencematch_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@imagereferencematch_server.tool
@wrapped_fn_tool
def get_imagereferencematch(
    imagereferencematch_id: str,
    fields: list[str] = [],
) -> str:
    obj = ImageReferenceMatch(imagereferencematch_id)
    return obj.api_get(fields=fields)
