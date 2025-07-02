"""BlindPig MCP Server."""

from typing import Any

from facebook_business.adobjects.blindpig import BlindPig
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBlindPig"
instructions = """
BlindPig MCP Server for Facebook Business API.

Provides typed access to all BlindPig operations.
"""

blindpig_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@blindpig_server.tool
@wrapped_fn_tool
def get_blindpig(
    blindpig_id: str,
    fields: list[str] = [],
) -> str:
    obj = BlindPig(blindpig_id)
    return obj.api_get(fields=fields)
