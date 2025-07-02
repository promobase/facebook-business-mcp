"""ManagedPartnerBusiness MCP Server."""

from typing import Any

from facebook_business.adobjects.managedpartnerbusiness import ManagedPartnerBusiness
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookManagedPartnerBusiness"
instructions = """
ManagedPartnerBusiness MCP Server for Facebook Business API.

Provides typed access to all ManagedPartnerBusiness operations.
"""

managedpartnerbusiness_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@managedpartnerbusiness_server.tool
@wrapped_fn_tool
def get_endpoint(
    managedpartnerbusiness_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ManagedPartnerBusiness(managedpartnerbusiness_id).get_endpoint(
        fields=fields, params=params
    )
