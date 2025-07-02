"""Canvas MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.canvas import Canvas
from fastmcp import FastMCP

from src.generated.models.canvas import CanvasField, CanvasGetPreViewsParams, CanvasUpdateParams
from src.generated.models.textwithentities import TextWithEntitiesField
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
    fields: list[CanvasField] = [],
) -> str:
    """Get a Canvas object by ID.

    Args:
        canvas_id: The ID of the Canvas.
        fields: Fields to retrieve. Available fields: See CanvasField type.
    """
    obj = Canvas(canvas_id)
    return obj.api_get(fields=fields)


@canvas_server.tool
@wrapped_fn_tool
def update_canvas(
    canvas_id: str,
    fields: list[CanvasField] = [],
    params: CanvasUpdateParams | dict = {},
) -> str:
    """Update a Canvas object.

    Args:
        canvas_id: The ID of the Canvas.
        fields: Fields to return after update. Available fields: See CanvasField type.
        params: Parameters to update. Available params: See CanvasUpdateParams type.
    """
    return Canvas(canvas_id).api_update(fields=fields, params=params)


# ---- Edge Methods (1) ----
@canvas_server.tool
@wrapped_fn_tool
def get_pre_views(
    canvas_id: str,
    fields: list[TextWithEntitiesField] = [],
    params: CanvasGetPreViewsParams | dict = {},
):
    """Get Pre Views for this Canvas.

    Args:
        canvas_id: The ID of the Canvas.
        fields: Fields to retrieve. Available fields: See TextWithEntitiesField type.
        params: Query parameters. Available params: See CanvasGetPreViewsParams type.
    """
    return Canvas(canvas_id).get_pre_views(fields=fields, params=params)
