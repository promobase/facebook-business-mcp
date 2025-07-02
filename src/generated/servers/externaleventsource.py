"""ExternalEventSource MCP Server."""

from typing import Any

from facebook_business.adobjects.externaleventsource import ExternalEventSource
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookExternalEventSource"
instructions = """
ExternalEventSource MCP Server for Facebook Business API.

Provides typed access to all ExternalEventSource operations.
"""

externaleventsource_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@externaleventsource_server.tool
@wrapped_fn_tool
def get_endpoint(
    externaleventsource_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ExternalEventSource(externaleventsource_id).get_endpoint(fields=fields, params=params)
