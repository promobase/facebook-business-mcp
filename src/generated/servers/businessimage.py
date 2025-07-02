"""BusinessImage MCP Server."""

from typing import Any

from facebook_business.adobjects.businessimage import BusinessImage
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessImage"
instructions = """
BusinessImage MCP Server for Facebook Business API.

Provides typed access to all BusinessImage operations.
"""

businessimage_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@businessimage_server.tool
@wrapped_fn_tool
def get_businessimage(
    businessimage_id: str,
    fields: list[str] = [],
) -> str:
    obj = BusinessImage(businessimage_id)
    return obj.api_get(fields=fields)
