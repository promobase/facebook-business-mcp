"""ALMAdAccountInfo MCP Server."""

from typing import Any

from facebook_business.adobjects.almadaccountinfo import ALMAdAccountInfo
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookALMAdAccountInfo"
instructions = """
ALMAdAccountInfo MCP Server for Facebook Business API.

Provides typed access to all ALMAdAccountInfo operations.
"""

almadaccountinfo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@almadaccountinfo_server.tool
@wrapped_fn_tool
def get_almadaccountinfo(
    almadaccountinfo_id: str,
    fields: list[str] = [],
) -> str:
    obj = ALMAdAccountInfo(almadaccountinfo_id)
    return obj.api_get(fields=fields)
