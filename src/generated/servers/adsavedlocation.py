"""AdSavedLocation MCP Server."""

from typing import Any

from facebook_business.adobjects.adsavedlocation import AdSavedLocation
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdSavedLocation"
instructions = """
AdSavedLocation MCP Server for Facebook Business API.

Provides typed access to all AdSavedLocation operations.
"""

adsavedlocation_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adsavedlocation_server.tool
@wrapped_fn_tool
def get_adsavedlocation(
    adsavedlocation_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdSavedLocation(adsavedlocation_id)
    return obj.api_get(fields=fields)
