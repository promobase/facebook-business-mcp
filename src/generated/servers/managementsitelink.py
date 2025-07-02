"""ManagementSiteLink MCP Server."""

from typing import Any

from facebook_business.adobjects.managementsitelink import ManagementSiteLink
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookManagementSiteLink"
instructions = """
ManagementSiteLink MCP Server for Facebook Business API.

Provides typed access to all ManagementSiteLink operations.
"""

managementsitelink_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@managementsitelink_server.tool
@wrapped_fn_tool
def get_managementsitelink(
    managementsitelink_id: str,
    fields: list[str] = [],
) -> str:
    obj = ManagementSiteLink(managementsitelink_id)
    return obj.api_get(fields=fields)
