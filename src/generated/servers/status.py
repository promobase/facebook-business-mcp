"""Status MCP Server."""

from typing import Any

from facebook_business.adobjects.status import Status
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = Status(status_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@status_server.tool
@wrapped_fn_tool
def create_like(
    status_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return Status(status_id).create_like(fields=fields, params=params)
