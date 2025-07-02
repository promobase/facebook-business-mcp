"""CanvasDynamicSetting MCP Server."""

from typing import Any

from facebook_business.adobjects.canvasdynamicsetting import CanvasDynamicSetting
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCanvasDynamicSetting"
instructions = """
CanvasDynamicSetting MCP Server for Facebook Business API.

Provides typed access to all CanvasDynamicSetting operations.
"""

canvasdynamicsetting_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@canvasdynamicsetting_server.tool
@wrapped_fn_tool
def get_canvasdynamicsetting(
    canvasdynamicsetting_id: str,
    fields: list[str] = [],
) -> str:
    obj = CanvasDynamicSetting(canvasdynamicsetting_id)
    return obj.api_get(fields=fields)
