"""Organization MCP Server."""

from typing import Any

from facebook_business.adobjects.organization import Organization
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookOrganization"
instructions = """
Organization MCP Server for Facebook Business API.

Provides typed access to all Organization operations.
"""

organization_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@organization_server.tool
@wrapped_fn_tool
def get_organization(
    organization_id: str,
    fields: list[str] = [],
) -> str:
    obj = Organization(organization_id)
    return obj.api_get(fields=fields)
