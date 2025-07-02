"""Status MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.status import Status
from fastmcp import FastMCP

from src.generated.models.status import StatusCreateLikeParams, StatusField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookStatus"
instructions = """
Status MCP Server for Facebook Business API.

Provides typed access to all Status operations.
"""

status_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@status_server.tool
@wrapped_fn_tool
def get_status(
    status_id: str,
    fields: list[StatusField] = [],
) -> str:
    """Get a Status object by ID.

    Args:
        status_id: The ID of the Status.
        fields: Fields to retrieve. Available fields: See StatusField type.
    """
    obj = Status(status_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@status_server.tool
@wrapped_fn_tool
def create_like(
    status_id: str,
    fields: list[str] = [],
    params: StatusCreateLikeParams | dict = {},
):
    """Create Like for this Status.

    Args:
        status_id: The ID of the Status.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See StatusCreateLikeParams type.
    """
    return Status(status_id).create_like(fields=fields, params=params)
