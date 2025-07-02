"""AppLinks MCP Server."""

from typing import Any

from facebook_business.adobjects.applinks import AppLinks
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAppLinks"
instructions = """
AppLinks MCP Server for Facebook Business API.

Provides typed access to all AppLinks operations.
"""

applinks_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@applinks_server.tool
@wrapped_fn_tool
def get_applinks(
    applinks_id: str,
    fields: list[str] = [],
) -> str:
    obj = AppLinks(applinks_id)
    return obj.api_get(fields=fields)
