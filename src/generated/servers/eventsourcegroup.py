"""EventSourceGroup MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.eventsourcegroup import EventSourceGroup
from fastmcp import FastMCP

from src.generated.models.eventsourcegroup import (
    EventSourceGroupCreateSharedAccountParams,
    EventSourceGroupField,
    EventSourceGroupUpdateParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookEventSourceGroup"
instructions = """
EventSourceGroup MCP Server for Facebook Business API.

Provides typed access to all EventSourceGroup operations.
"""

eventsourcegroup_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@eventsourcegroup_server.tool
@wrapped_fn_tool
def get_eventsourcegroup(
    eventsourcegroup_id: str,
    fields: list[EventSourceGroupField] = [],
) -> str:
    """Get a EventSourceGroup object by ID.

    Args:
        eventsourcegroup_id: The ID of the EventSourceGroup.
        fields: Fields to retrieve. Available fields: See EventSourceGroupField type.
    """
    obj = EventSourceGroup(eventsourcegroup_id)
    return obj.api_get(fields=fields)


@eventsourcegroup_server.tool
@wrapped_fn_tool
def update_eventsourcegroup(
    eventsourcegroup_id: str,
    fields: list[EventSourceGroupField] = [],
    params: EventSourceGroupUpdateParams | dict = {},
) -> str:
    """Update a EventSourceGroup object.

    Args:
        eventsourcegroup_id: The ID of the EventSourceGroup.
        fields: Fields to return after update. Available fields: See EventSourceGroupField type.
        params: Parameters to update. Available params: See EventSourceGroupUpdateParams type.
    """
    return EventSourceGroup(eventsourcegroup_id).api_update(fields=fields, params=params)


# ---- Edge Methods (1) ----
@eventsourcegroup_server.tool
@wrapped_fn_tool
def create_shared_account(
    eventsourcegroup_id: str,
    fields: list[str] = [],
    params: EventSourceGroupCreateSharedAccountParams | dict = {},
):
    """Create Shared Account for this EventSourceGroup.

    Args:
        eventsourcegroup_id: The ID of the EventSourceGroup.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See EventSourceGroupCreateSharedAccountParams type.
    """
    return EventSourceGroup(eventsourcegroup_id).create_shared_account(fields=fields, params=params)
