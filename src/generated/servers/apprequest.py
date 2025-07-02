"""AppRequest MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.apprequest import AppRequest
from fastmcp import FastMCP

from src.generated.models.apprequest import AppRequestField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAppRequest"
instructions = """
AppRequest MCP Server for Facebook Business API.

Provides typed access to all AppRequest operations.
"""

apprequest_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@apprequest_server.tool
@wrapped_fn_tool
def get_apprequest(
    apprequest_id: str,
    fields: list[AppRequestField] = [],
) -> str:
    """Get a AppRequest object by ID.

    Args:
        apprequest_id: The ID of the AppRequest.
        fields: Fields to retrieve. Available fields: See AppRequestField type.
    """
    obj = AppRequest(apprequest_id)
    return obj.api_get(fields=fields)


@apprequest_server.tool
@wrapped_fn_tool
def delete_apprequest(
    apprequest_id: str,
) -> str:
    """Delete a AppRequest object.

    Args:
        apprequest_id: The ID of the AppRequest.
    """
    return AppRequest(apprequest_id).api_delete()
