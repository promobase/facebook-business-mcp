"""CRMAddress MCP Server."""

from typing import Any

from facebook_business.adobjects.crmaddress import CRMAddress
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCRMAddress"
instructions = """
CRMAddress MCP Server for Facebook Business API.

Provides typed access to all CRMAddress operations.
"""

crmaddress_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@crmaddress_server.tool
@wrapped_fn_tool
def get_crmaddress(
    crmaddress_id: str,
    fields: list[str] = [],
) -> str:
    obj = CRMAddress(crmaddress_id)
    return obj.api_get(fields=fields)
