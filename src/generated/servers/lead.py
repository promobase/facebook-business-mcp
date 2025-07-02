"""Lead MCP Server."""

from typing import Any

from facebook_business.adobjects.lead import Lead
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLead"
instructions = """
Lead MCP Server for Facebook Business API.

Provides typed access to all Lead operations.
"""

lead_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@lead_server.tool
@wrapped_fn_tool
def get_lead(
    lead_id: str,
    fields: list[str] = [],
) -> str:
    obj = Lead(lead_id)
    return obj.api_get(fields=fields)


@lead_server.tool
@wrapped_fn_tool
def delete_lead(
    lead_id: str,
) -> str:
    return Lead(lead_id).api_delete()
