"""CopyrightOwnershipTransfer MCP Server."""

from typing import Any

from facebook_business.adobjects.copyrightownershiptransfer import CopyrightOwnershipTransfer
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCopyrightOwnershipTransfer"
instructions = """
CopyrightOwnershipTransfer MCP Server for Facebook Business API.

Provides typed access to all CopyrightOwnershipTransfer operations.
"""

copyrightownershiptransfer_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@copyrightownershiptransfer_server.tool
@wrapped_fn_tool
def get_copyrightownershiptransfer(
    copyrightownershiptransfer_id: str,
    fields: list[str] = [],
) -> str:
    obj = CopyrightOwnershipTransfer(copyrightownershiptransfer_id)
    return obj.api_get(fields=fields)
