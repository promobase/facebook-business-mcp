"""AdLightAdgroup MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adlightadgroup import AdLightAdgroup
from fastmcp import FastMCP

from src.generated.models.adlightadgroup import AdLightAdgroupField
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
    fields: list[AdLightAdgroupField] = [],
) -> str:
    """Get a AdLightAdgroup object by ID.

    Args:
        adlightadgroup_id: The ID of the AdLightAdgroup.
        fields: Fields to retrieve. Available fields: See AdLightAdgroupField type.
    """
    obj = AdLightAdgroup(adlightadgroup_id)
    return obj.api_get(fields=fields)
