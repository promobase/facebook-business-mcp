"""FantasyGame MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.fantasygame import FantasyGame
from fastmcp import FastMCP

from src.generated.models.fantasygame import FantasyGameField
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
    fields: list[FantasyGameField] = [],
) -> str:
    """Get a FantasyGame object by ID.

    Args:
        fantasygame_id: The ID of the FantasyGame.
        fields: Fields to retrieve. Available fields: See FantasyGameField type.
    """
    obj = FantasyGame(fantasygame_id)
    return obj.api_get(fields=fields)
