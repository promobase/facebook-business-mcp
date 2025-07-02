"""GeoGatingPolicy MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.geogatingpolicy import GeoGatingPolicy
from fastmcp import FastMCP

from src.generated.models.geogatingpolicy import GeoGatingPolicyField
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
    fields: list[GeoGatingPolicyField] = [],
) -> str:
    """Get a GeoGatingPolicy object by ID.

    Args:
        geogatingpolicy_id: The ID of the GeoGatingPolicy.
        fields: Fields to retrieve. Available fields: See GeoGatingPolicyField type.
    """
    obj = GeoGatingPolicy(geogatingpolicy_id)
    return obj.api_get(fields=fields)
