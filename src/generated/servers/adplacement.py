"""AdPlacement MCP Server."""

from typing import Any

from facebook_business.adobjects.adplacement import AdPlacement
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdPlacement"
instructions = """
AdPlacement MCP Server for Facebook Business API.

Provides typed access to all AdPlacement operations.
"""

adplacement_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adplacement_server.tool
@wrapped_fn_tool
def get_adplacement(
    adplacement_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdPlacement(adplacement_id)
    return obj.api_get(fields=fields)
