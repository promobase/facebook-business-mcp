"""BusinessTag MCP Server."""

from typing import Any

from facebook_business.adobjects.businesstag import BusinessTag
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessTag"
instructions = """
BusinessTag MCP Server for Facebook Business API.

Provides typed access to all BusinessTag operations.
"""

businesstag_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@businesstag_server.tool
@wrapped_fn_tool
def get_businesstag(
    businesstag_id: str,
    fields: list[str] = [],
) -> str:
    obj = BusinessTag(businesstag_id)
    return obj.api_get(fields=fields)
