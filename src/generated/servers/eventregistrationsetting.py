"""EventRegistrationSetting MCP Server."""

from typing import Any

from facebook_business.adobjects.eventregistrationsetting import EventRegistrationSetting
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookEventRegistrationSetting"
instructions = """
EventRegistrationSetting MCP Server for Facebook Business API.

Provides typed access to all EventRegistrationSetting operations.
"""

eventregistrationsetting_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@eventregistrationsetting_server.tool
@wrapped_fn_tool
def get_eventregistrationsetting(
    eventregistrationsetting_id: str,
    fields: list[str] = [],
) -> str:
    obj = EventRegistrationSetting(eventregistrationsetting_id)
    return obj.api_get(fields=fields)
