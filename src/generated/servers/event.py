"""Event MCP Server."""

from typing import Any

from facebook_business.adobjects.event import Event
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookEvent"
instructions = """
Event MCP Server for Facebook Business API.

Provides typed access to all Event operations.
"""

event_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@event_server.tool
@wrapped_fn_tool
def get_event(
    event_id: str,
    fields: list[str] = [],
) -> str:
    obj = Event(event_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@event_server.tool
@wrapped_fn_tool
def create_live_video(
    event_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Event(event_id).create_live_video(fields=fields, params=params)
