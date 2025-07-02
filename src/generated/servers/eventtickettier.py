"""EventTicketTier MCP Server."""

from typing import Any

from facebook_business.adobjects.eventtickettier import EventTicketTier
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookEventTicketTier"
instructions = """
EventTicketTier MCP Server for Facebook Business API.

Provides typed access to all EventTicketTier operations.
"""

eventtickettier_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@eventtickettier_server.tool
@wrapped_fn_tool
def get_eventtickettier(
    eventtickettier_id: str,
    fields: list[str] = [],
) -> str:
    obj = EventTicketTier(eventtickettier_id)
    return obj.api_get(fields=fields)
