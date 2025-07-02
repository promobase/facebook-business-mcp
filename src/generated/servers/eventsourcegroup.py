"""EventSourceGroup MCP Server."""

from typing import Any

from facebook_business.adobjects.eventsourcegroup import EventSourceGroup
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = EventSourceGroup(eventsourcegroup_id)
    return obj.api_get(fields=fields)


@eventsourcegroup_server.tool
@wrapped_fn_tool
def update_eventsourcegroup(
    eventsourcegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return EventSourceGroup(eventsourcegroup_id).api_update(fields=fields, params=params)


# ---- Edge Methods (1) ----
@eventsourcegroup_server.tool
@wrapped_fn_tool
def create_shared_account(
    eventsourcegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return EventSourceGroup(eventsourcegroup_id).create_shared_account(fields=fields, params=params)
