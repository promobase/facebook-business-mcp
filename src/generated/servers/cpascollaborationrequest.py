"""CPASCollaborationRequest MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.cpascollaborationrequest import CPASCollaborationRequest
from fastmcp import FastMCP

from src.generated.models.cpascollaborationrequest import CPASCollaborationRequestField
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
    fields: list[CPASCollaborationRequestField] = [],
) -> str:
    """Get a CPASCollaborationRequest object by ID.

    Args:
        cpascollaborationrequest_id: The ID of the CPASCollaborationRequest.
        fields: Fields to retrieve. Available fields: See CPASCollaborationRequestField type.
    """
    obj = CPASCollaborationRequest(cpascollaborationrequest_id)
    return obj.api_get(fields=fields)
