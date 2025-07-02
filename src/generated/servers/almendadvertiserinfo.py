"""ALMEndAdvertiserInfo MCP Server."""

from typing import Any

from facebook_business.adobjects.almendadvertiserinfo import ALMEndAdvertiserInfo
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookALMEndAdvertiserInfo"
instructions = """
ALMEndAdvertiserInfo MCP Server for Facebook Business API.

Provides typed access to all ALMEndAdvertiserInfo operations.
"""

almendadvertiserinfo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@almendadvertiserinfo_server.tool
@wrapped_fn_tool
def get_almendadvertiserinfo(
    almendadvertiserinfo_id: str,
    fields: list[str] = [],
) -> str:
    obj = ALMEndAdvertiserInfo(almendadvertiserinfo_id)
    return obj.api_get(fields=fields)
