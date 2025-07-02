"""EventTicketSetting MCP Server."""

from typing import Any

from facebook_business.adobjects.eventticketsetting import EventTicketSetting
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookEventTicketSetting"
instructions = """
EventTicketSetting MCP Server for Facebook Business API.

Provides typed access to all EventTicketSetting operations.
"""

eventticketsetting_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@eventticketsetting_server.tool
@wrapped_fn_tool
def get_eventticketsetting(
    eventticketsetting_id: str,
    fields: list[str] = [],
) -> str:
    obj = EventTicketSetting(eventticketsetting_id)
    return obj.api_get(fields=fields)
