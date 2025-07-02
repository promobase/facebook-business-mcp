"""FantasyGame MCP Server."""

from typing import Any

from facebook_business.adobjects.fantasygame import FantasyGame
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookFantasyGame"
instructions = """
FantasyGame MCP Server for Facebook Business API.

Provides typed access to all FantasyGame operations.
"""

fantasygame_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@fantasygame_server.tool
@wrapped_fn_tool
def get_fantasygame(
    fantasygame_id: str,
    fields: list[str] = [],
) -> str:
    obj = FantasyGame(fantasygame_id)
    return obj.api_get(fields=fields)
