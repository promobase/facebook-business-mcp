"""IGBoostMediaAd MCP Server."""

from typing import Any

from facebook_business.adobjects.igboostmediaad import IGBoostMediaAd
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGBoostMediaAd"
instructions = """
IGBoostMediaAd MCP Server for Facebook Business API.

Provides typed access to all IGBoostMediaAd operations.
"""

igboostmediaad_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@igboostmediaad_server.tool
@wrapped_fn_tool
def get_igboostmediaad(
    igboostmediaad_id: str,
    fields: list[str] = [],
) -> str:
    obj = IGBoostMediaAd(igboostmediaad_id)
    return obj.api_get(fields=fields)
