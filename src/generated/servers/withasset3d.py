"""WithAsset3D MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.withasset3d import WithAsset3D
from fastmcp import FastMCP

from src.generated.models.withasset3d import WithAsset3DField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWithAsset3D"
instructions = """
WithAsset3D MCP Server for Facebook Business API.

Provides typed access to all WithAsset3D operations.
"""

withasset3d_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@withasset3d_server.tool
@wrapped_fn_tool
def get_withasset3d(
    withasset3d_id: str,
    fields: list[WithAsset3DField] = [],
) -> str:
    """Get a WithAsset3D object by ID.

    Args:
        withasset3d_id: The ID of the WithAsset3D.
        fields: Fields to retrieve. Available fields: See WithAsset3DField type.
    """
    obj = WithAsset3D(withasset3d_id)
    return obj.api_get(fields=fields)
