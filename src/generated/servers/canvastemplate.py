"""CanvasTemplate MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.canvastemplate import CanvasTemplate
from fastmcp import FastMCP

from src.generated.models.canvastemplate import CanvasTemplateField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCanvasTemplate"
instructions = """
CanvasTemplate MCP Server for Facebook Business API.

Provides typed access to all CanvasTemplate operations.
"""

canvastemplate_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@canvastemplate_server.tool
@wrapped_fn_tool
def get_canvastemplate(
    canvastemplate_id: str,
    fields: list[CanvasTemplateField] = [],
) -> str:
    """Get a CanvasTemplate object by ID.

    Args:
        canvastemplate_id: The ID of the CanvasTemplate.
        fields: Fields to retrieve. Available fields: See CanvasTemplateField type.
    """
    obj = CanvasTemplate(canvastemplate_id)
    return obj.api_get(fields=fields)
