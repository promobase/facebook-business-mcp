"""AdColumnSizes MCP Server."""

from typing import Any

from facebook_business.adobjects.adcolumnsizes import AdColumnSizes
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdColumnSizes"
instructions = """
AdColumnSizes MCP Server for Facebook Business API.

Provides typed access to all AdColumnSizes operations.
"""

adcolumnsizes_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adcolumnsizes_server.tool
@wrapped_fn_tool
def get_adcolumnsizes(
    adcolumnsizes_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdColumnSizes(adcolumnsizes_id)
    return obj.api_get(fields=fields)
