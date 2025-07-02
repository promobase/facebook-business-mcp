"""ALMEndAdvertiserInfo MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.almendadvertiserinfo import ALMEndAdvertiserInfo
from fastmcp import FastMCP

from src.generated.models.almendadvertiserinfo import ALMEndAdvertiserInfoField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookALMEndAdvertiserInfo"
instructions = """
ALMEndAdvertiserInfo MCP Server for Facebook Business API.

Provides typed access to all ALMEndAdvertiserInfo operations.
"""

almendadvertiserinfo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@almendadvertiserinfo_server.tool
@wrapped_fn_tool
def get_almendadvertiserinfo(
    almendadvertiserinfo_id: str,
    fields: list[ALMEndAdvertiserInfoField] = [],
) -> str:
    """Get a ALMEndAdvertiserInfo object by ID.

    Args:
        almendadvertiserinfo_id: The ID of the ALMEndAdvertiserInfo.
        fields: Fields to retrieve. Available fields: See ALMEndAdvertiserInfoField type.
    """
    obj = ALMEndAdvertiserInfo(almendadvertiserinfo_id)
    return obj.api_get(fields=fields)
