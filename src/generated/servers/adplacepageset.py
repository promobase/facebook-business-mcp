"""AdPlacePageSet MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adplacepageset import AdPlacePageSet
from fastmcp import FastMCP

from src.generated.models.adplacepageset import AdPlacePageSetField
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
    fields: list[AdPlacePageSetField] = [],
) -> str:
    """Get a AdPlacePageSet object by ID.

    Args:
        adplacepageset_id: The ID of the AdPlacePageSet.
        fields: Fields to retrieve. Available fields: See AdPlacePageSetField type.
    """
    obj = AdPlacePageSet(adplacepageset_id)
    return obj.api_get(fields=fields)
