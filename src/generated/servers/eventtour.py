"""EventTour MCP Server."""

from typing import Any

from facebook_business.adobjects.eventtour import EventTour
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookEventTour"
instructions = """
EventTour MCP Server for Facebook Business API.

Provides typed access to all EventTour operations.
"""

eventtour_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@eventtour_server.tool
@wrapped_fn_tool
def get_eventtour(
    eventtour_id: str,
    fields: list[str] = [],
) -> str:
    obj = EventTour(eventtour_id)
    return obj.api_get(fields=fields)
