"""IGBoostMediaAd MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.igboostmediaad import IGBoostMediaAd
from fastmcp import FastMCP

from src.generated.models.igboostmediaad import IGBoostMediaAdField
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
    fields: list[IGBoostMediaAdField] = [],
) -> str:
    """Get a IGBoostMediaAd object by ID.

    Args:
        igboostmediaad_id: The ID of the IGBoostMediaAd.
        fields: Fields to retrieve. Available fields: See IGBoostMediaAdField type.
    """
    obj = IGBoostMediaAd(igboostmediaad_id)
    return obj.api_get(fields=fields)
