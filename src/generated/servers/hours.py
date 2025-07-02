"""Hours MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.hours import Hours
from fastmcp import FastMCP

from src.generated.models.hours import HoursField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookHours"
instructions = """
Hours MCP Server for Facebook Business API.

Provides typed access to all Hours operations.
"""

hours_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@hours_server.tool
@wrapped_fn_tool
def get_hours(
    hours_id: str,
    fields: list[HoursField] = [],
) -> str:
    """Get a Hours object by ID.

    Args:
        hours_id: The ID of the Hours.
        fields: Fields to retrieve. Available fields: See HoursField type.
    """
    obj = Hours(hours_id)
    return obj.api_get(fields=fields)
