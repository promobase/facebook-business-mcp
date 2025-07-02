"""AdAccountUser MCP Server."""

from typing import Any

from facebook_business.adobjects.adaccountuser import AdAccountUser
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdAccountUser"
instructions = """
AdAccountUser MCP Server for Facebook Business API.

Provides typed access to all AdAccountUser operations.
"""

adaccountuser_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@adaccountuser_server.tool
@wrapped_fn_tool
def get_endpoint(
    adaccountuser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccountUser(adaccountuser_id).get_endpoint(fields=fields, params=params)
