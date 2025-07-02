"""LifeEvent MCP Server."""

from typing import Any

from facebook_business.adobjects.lifeevent import LifeEvent
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLifeEvent"
instructions = """
LifeEvent MCP Server for Facebook Business API.

Provides typed access to all LifeEvent operations.
"""

lifeevent_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@lifeevent_server.tool
@wrapped_fn_tool
def get_lifeevent(
    lifeevent_id: str,
    fields: list[str] = [],
) -> str:
    obj = LifeEvent(lifeevent_id)
    return obj.api_get(fields=fields)
