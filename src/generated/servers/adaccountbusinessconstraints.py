"""AdAccountBusinessConstraints MCP Server."""

from typing import Any

from facebook_business.adobjects.adaccountbusinessconstraints import AdAccountBusinessConstraints
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdAccountBusinessConstraints"
instructions = """
AdAccountBusinessConstraints MCP Server for Facebook Business API.

Provides typed access to all AdAccountBusinessConstraints operations.
"""

adaccountbusinessconstraints_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@adaccountbusinessconstraints_server.tool
@wrapped_fn_tool
def get_endpoint(
    adaccountbusinessconstraints_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccountBusinessConstraints(adaccountbusinessconstraints_id).get_endpoint(
        fields=fields, params=params
    )
