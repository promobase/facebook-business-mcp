"""AdsCreationSavedState MCP Server."""

from typing import Any

from facebook_business.adobjects.adscreationsavedstate import AdsCreationSavedState
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsCreationSavedState"
instructions = """
AdsCreationSavedState MCP Server for Facebook Business API.

Provides typed access to all AdsCreationSavedState operations.
"""

adscreationsavedstate_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adscreationsavedstate_server.tool
@wrapped_fn_tool
def get_adscreationsavedstate(
    adscreationsavedstate_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdsCreationSavedState(adscreationsavedstate_id)
    return obj.api_get(fields=fields)
