"""BusinessRequest MCP Server."""

from typing import Any

from facebook_business.adobjects.businessrequest import BusinessRequest
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessRequest"
instructions = """
BusinessRequest MCP Server for Facebook Business API.

Provides typed access to all BusinessRequest operations.
"""

businessrequest_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@businessrequest_server.tool
@wrapped_fn_tool
def get_businessrequest(
    businessrequest_id: str,
    fields: list[str] = [],
) -> str:
    obj = BusinessRequest(businessrequest_id)
    return obj.api_get(fields=fields)
