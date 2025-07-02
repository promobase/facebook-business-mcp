"""IGUpcomingEvent MCP Server."""

from typing import Any

from facebook_business.adobjects.igupcomingevent import IGUpcomingEvent
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGUpcomingEvent"
instructions = """
IGUpcomingEvent MCP Server for Facebook Business API.

Provides typed access to all IGUpcomingEvent operations.
"""

igupcomingevent_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@igupcomingevent_server.tool
@wrapped_fn_tool
def get_igupcomingevent(
    igupcomingevent_id: str,
    fields: list[str] = [],
) -> str:
    obj = IGUpcomingEvent(igupcomingevent_id)
    return obj.api_get(fields=fields)


@igupcomingevent_server.tool
@wrapped_fn_tool
def update_igupcomingevent(
    igupcomingevent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return IGUpcomingEvent(igupcomingevent_id).api_update(fields=fields, params=params)
