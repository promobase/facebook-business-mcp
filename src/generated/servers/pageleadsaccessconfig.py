"""PageLeadsAccessConfig MCP Server."""

from typing import Any

from facebook_business.adobjects.pageleadsaccessconfig import PageLeadsAccessConfig
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPageLeadsAccessConfig"
instructions = """
PageLeadsAccessConfig MCP Server for Facebook Business API.

Provides typed access to all PageLeadsAccessConfig operations.
"""

pageleadsaccessconfig_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@pageleadsaccessconfig_server.tool
@wrapped_fn_tool
def get_pageleadsaccessconfig(
    pageleadsaccessconfig_id: str,
    fields: list[str] = [],
) -> str:
    obj = PageLeadsAccessConfig(pageleadsaccessconfig_id)
    return obj.api_get(fields=fields)
