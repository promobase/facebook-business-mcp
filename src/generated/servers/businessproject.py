"""BusinessProject MCP Server."""

from typing import Any

from facebook_business.adobjects.businessproject import BusinessProject
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessProject"
instructions = """
BusinessProject MCP Server for Facebook Business API.

Provides typed access to all BusinessProject operations.
"""

businessproject_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@businessproject_server.tool
@wrapped_fn_tool
def get_businessproject(
    businessproject_id: str,
    fields: list[str] = [],
) -> str:
    obj = BusinessProject(businessproject_id)
    return obj.api_get(fields=fields)
