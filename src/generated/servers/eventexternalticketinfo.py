"""EventExternalTicketInfo MCP Server."""

from typing import Any

from facebook_business.adobjects.eventexternalticketinfo import EventExternalTicketInfo
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookEventExternalTicketInfo"
instructions = """
EventExternalTicketInfo MCP Server for Facebook Business API.

Provides typed access to all EventExternalTicketInfo operations.
"""

eventexternalticketinfo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@eventexternalticketinfo_server.tool
@wrapped_fn_tool
def get_eventexternalticketinfo(
    eventexternalticketinfo_id: str,
    fields: list[str] = [],
) -> str:
    obj = EventExternalTicketInfo(eventexternalticketinfo_id)
    return obj.api_get(fields=fields)
