"""FranchiseProgram MCP Server."""

from typing import Any

from facebook_business.adobjects.franchiseprogram import FranchiseProgram
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookFranchiseProgram"
instructions = """
FranchiseProgram MCP Server for Facebook Business API.

Provides typed access to all FranchiseProgram operations.
"""

franchiseprogram_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@franchiseprogram_server.tool
@wrapped_fn_tool
def get_franchiseprogram(
    franchiseprogram_id: str,
    fields: list[str] = [],
) -> str:
    obj = FranchiseProgram(franchiseprogram_id)
    return obj.api_get(fields=fields)
