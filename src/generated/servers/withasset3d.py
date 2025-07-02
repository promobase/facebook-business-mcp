"""WithAsset3D MCP Server."""

from typing import Any

from facebook_business.adobjects.withasset3d import WithAsset3D
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = WithAsset3D(withasset3d_id)
    return obj.api_get(fields=fields)
