"""ALMEvent MCP Server."""

from typing import Any

from facebook_business.adobjects.almevent import ALMEvent
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookALMEvent"
instructions = """
ALMEvent MCP Server for Facebook Business API.

Provides typed access to all ALMEvent operations.
"""

almevent_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@almevent_server.tool
@wrapped_fn_tool
def get_almevent(
    almevent_id: str,
    fields: list[str] = [],
) -> str:
    obj = ALMEvent(almevent_id)
    return obj.api_get(fields=fields)
