"""CloudGame MCP Server."""

from typing import Any

from facebook_business.adobjects.cloudgame import CloudGame
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = CloudGame(cloudgame_id)
    return obj.api_get(fields=fields)
