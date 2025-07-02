"""WoodhengeSupporter MCP Server."""

from typing import Any

from facebook_business.adobjects.woodhengesupporter import WoodhengeSupporter
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWoodhengeSupporter"
instructions = """
WoodhengeSupporter MCP Server for Facebook Business API.

Provides typed access to all WoodhengeSupporter operations.
"""

woodhengesupporter_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@woodhengesupporter_server.tool
@wrapped_fn_tool
def get_woodhengesupporter(
    woodhengesupporter_id: str,
    fields: list[str] = [],
) -> str:
    obj = WoodhengeSupporter(woodhengesupporter_id)
    return obj.api_get(fields=fields)
