"""GeoGatingPolicy MCP Server."""

from typing import Any

from facebook_business.adobjects.geogatingpolicy import GeoGatingPolicy
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookGeoGatingPolicy"
instructions = """
GeoGatingPolicy MCP Server for Facebook Business API.

Provides typed access to all GeoGatingPolicy operations.
"""

geogatingpolicy_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@geogatingpolicy_server.tool
@wrapped_fn_tool
def get_geogatingpolicy(
    geogatingpolicy_id: str,
    fields: list[str] = [],
) -> str:
    obj = GeoGatingPolicy(geogatingpolicy_id)
    return obj.api_get(fields=fields)
