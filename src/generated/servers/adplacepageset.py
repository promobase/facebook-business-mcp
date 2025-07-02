"""AdPlacePageSet MCP Server."""

from typing import Any

from facebook_business.adobjects.adplacepageset import AdPlacePageSet
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdPlacePageSet"
instructions = """
AdPlacePageSet MCP Server for Facebook Business API.

Provides typed access to all AdPlacePageSet operations.
"""

adplacepageset_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adplacepageset_server.tool
@wrapped_fn_tool
def get_adplacepageset(
    adplacepageset_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdPlacePageSet(adplacepageset_id)
    return obj.api_get(fields=fields)
