"""IGBCAdsPermission MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.igbcadspermission import IGBCAdsPermission
from fastmcp import FastMCP

from src.generated.models.igbcadspermission import IGBCAdsPermissionField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGBCAdsPermission"
instructions = """
IGBCAdsPermission MCP Server for Facebook Business API.

Provides typed access to all IGBCAdsPermission operations.
"""

igbcadspermission_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@igbcadspermission_server.tool
@wrapped_fn_tool
def get_igbcadspermission(
    igbcadspermission_id: str,
    fields: list[IGBCAdsPermissionField] = [],
) -> str:
    """Get a IGBCAdsPermission object by ID.

    Args:
        igbcadspermission_id: The ID of the IGBCAdsPermission.
        fields: Fields to retrieve. Available fields: See IGBCAdsPermissionField type.
    """
    obj = IGBCAdsPermission(igbcadspermission_id)
    return obj.api_get(fields=fields)
