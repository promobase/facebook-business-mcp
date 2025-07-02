"""BusinessVideo MCP Server."""

from typing import Any

from facebook_business.adobjects.businessvideo import BusinessVideo
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessVideo"
instructions = """
BusinessVideo MCP Server for Facebook Business API.

Provides typed access to all BusinessVideo operations.
"""

businessvideo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@businessvideo_server.tool
@wrapped_fn_tool
def get_businessvideo(
    businessvideo_id: str,
    fields: list[str] = [],
) -> str:
    obj = BusinessVideo(businessvideo_id)
    return obj.api_get(fields=fields)
