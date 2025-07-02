"""CopyrightMediaMisuse MCP Server."""

from typing import Any

from facebook_business.adobjects.copyrightmediamisuse import CopyrightMediaMisuse
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCopyrightMediaMisuse"
instructions = """
CopyrightMediaMisuse MCP Server for Facebook Business API.

Provides typed access to all CopyrightMediaMisuse operations.
"""

copyrightmediamisuse_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@copyrightmediamisuse_server.tool
@wrapped_fn_tool
def get_copyrightmediamisuse(
    copyrightmediamisuse_id: str,
    fields: list[str] = [],
) -> str:
    obj = CopyrightMediaMisuse(copyrightmediamisuse_id)
    return obj.api_get(fields=fields)
