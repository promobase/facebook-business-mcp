"""CPASCollaborationRequest MCP Server."""

from typing import Any

from facebook_business.adobjects.cpascollaborationrequest import CPASCollaborationRequest
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCPASCollaborationRequest"
instructions = """
CPASCollaborationRequest MCP Server for Facebook Business API.

Provides typed access to all CPASCollaborationRequest operations.
"""

cpascollaborationrequest_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@cpascollaborationrequest_server.tool
@wrapped_fn_tool
def get_cpascollaborationrequest(
    cpascollaborationrequest_id: str,
    fields: list[str] = [],
) -> str:
    obj = CPASCollaborationRequest(cpascollaborationrequest_id)
    return obj.api_get(fields=fields)
