"""Canvas MCP Server."""

from typing import Any

from facebook_business.adobjects.canvas import Canvas
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCanvas"
instructions = """
Canvas MCP Server for Facebook Business API.

Provides typed access to all Canvas operations.
"""

canvas_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@canvas_server.tool
@wrapped_fn_tool
def get_canvas(
    canvas_id: str,
    fields: list[str] = [],
) -> str:
    obj = Canvas(canvas_id)
    return obj.api_get(fields=fields)


@canvas_server.tool
@wrapped_fn_tool
def update_canvas(
    canvas_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Canvas(canvas_id).api_update(fields=fields, params=params)


# ---- Edge Methods (1) ----
@canvas_server.tool
@wrapped_fn_tool
def get_pre_views(
    canvas_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Canvas(canvas_id).get_pre_views(fields=fields, params=params)
