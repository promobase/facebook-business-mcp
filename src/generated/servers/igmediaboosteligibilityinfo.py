"""IGMediaBoostEligibilityInfo MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.igmediaboosteligibilityinfo import IGMediaBoostEligibilityInfo
from fastmcp import FastMCP

from src.generated.models.igmediaboosteligibilityinfo import IGMediaBoostEligibilityInfoField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGMediaBoostEligibilityInfo"
instructions = """
IGMediaBoostEligibilityInfo MCP Server for Facebook Business API.

Provides typed access to all IGMediaBoostEligibilityInfo operations.
"""

igmediaboosteligibilityinfo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@igmediaboosteligibilityinfo_server.tool
@wrapped_fn_tool
def get_igmediaboosteligibilityinfo(
    igmediaboosteligibilityinfo_id: str,
    fields: list[IGMediaBoostEligibilityInfoField] = [],
) -> str:
    """Get a IGMediaBoostEligibilityInfo object by ID.

    Args:
        igmediaboosteligibilityinfo_id: The ID of the IGMediaBoostEligibilityInfo.
        fields: Fields to retrieve. Available fields: See IGMediaBoostEligibilityInfoField type.
    """
    obj = IGMediaBoostEligibilityInfo(igmediaboosteligibilityinfo_id)
    return obj.api_get(fields=fields)
