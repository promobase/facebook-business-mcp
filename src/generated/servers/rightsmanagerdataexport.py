"""RightsManagerDataExport MCP Server."""

from typing import Any

from facebook_business.adobjects.rightsmanagerdataexport import RightsManagerDataExport
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookRightsManagerDataExport"
instructions = """
RightsManagerDataExport MCP Server for Facebook Business API.

Provides typed access to all RightsManagerDataExport operations.
"""

rightsmanagerdataexport_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@rightsmanagerdataexport_server.tool
@wrapped_fn_tool
def get_rightsmanagerdataexport(
    rightsmanagerdataexport_id: str,
    fields: list[str] = [],
) -> str:
    obj = RightsManagerDataExport(rightsmanagerdataexport_id)
    return obj.api_get(fields=fields)
