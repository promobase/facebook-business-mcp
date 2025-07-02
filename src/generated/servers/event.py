"""Event MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.event import Event
from fastmcp import FastMCP

from src.generated.models.event import EventCreateLiveVideoParams, EventField
from src.generated.models.livevideo import LiveVideoField
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
    fields: list[EventField] = [],
) -> str:
    """Get a Event object by ID.

    Args:
        event_id: The ID of the Event.
        fields: Fields to retrieve. Available fields: See EventField type.
    """
    obj = Event(event_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@event_server.tool
@wrapped_fn_tool
def create_live_video(
    event_id: str,
    fields: list[str] = [],
    params: EventCreateLiveVideoParams | dict = {},
):
    """Create Live Video for this Event.

    Args:
        event_id: The ID of the Event.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See EventCreateLiveVideoParams type.
    """
    return Event(event_id).create_live_video(fields=fields, params=params)
