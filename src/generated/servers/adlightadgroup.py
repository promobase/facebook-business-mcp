"""AdLightAdgroup MCP Server."""

from typing import Any

from facebook_business.adobjects.adlightadgroup import AdLightAdgroup
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdLightAdgroup"
instructions = """
AdLightAdgroup MCP Server for Facebook Business API.

Provides typed access to all AdLightAdgroup operations.
"""

adlightadgroup_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adlightadgroup_server.tool
@wrapped_fn_tool
def get_adlightadgroup(
    adlightadgroup_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdLightAdgroup(adlightadgroup_id)
    return obj.api_get(fields=fields)
