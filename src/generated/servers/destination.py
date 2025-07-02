"""Destination MCP Server."""

from typing import Any

from facebook_business.adobjects.destination import Destination
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookDestination"
instructions = """
Destination MCP Server for Facebook Business API.

Provides typed access to all Destination operations.
"""

destination_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@destination_server.tool
@wrapped_fn_tool
def get_destination(
    destination_id: str,
    fields: list[str] = [],
) -> str:
    obj = Destination(destination_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@destination_server.tool
@wrapped_fn_tool
def get_override_details(
    destination_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Destination(destination_id).get_override_details(fields=fields, params=params)
