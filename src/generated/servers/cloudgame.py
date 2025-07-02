"""CloudGame MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.cloudgame import CloudGame
from fastmcp import FastMCP

from src.generated.models.cloudgame import CloudGameField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCloudGame"
instructions = """
CloudGame MCP Server for Facebook Business API.

Provides typed access to all CloudGame operations.
"""

cloudgame_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@cloudgame_server.tool
@wrapped_fn_tool
def get_cloudgame(
    cloudgame_id: str,
    fields: list[CloudGameField] = [],
) -> str:
    """Get a CloudGame object by ID.

    Args:
        cloudgame_id: The ID of the CloudGame.
        fields: Fields to retrieve. Available fields: See CloudGameField type.
    """
    obj = CloudGame(cloudgame_id)
    return obj.api_get(fields=fields)
