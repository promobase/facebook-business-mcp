"""IGMediaBoostEligibilityInfo MCP Server."""

from typing import Any

from facebook_business.adobjects.igmediaboosteligibilityinfo import IGMediaBoostEligibilityInfo
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = IGMediaBoostEligibilityInfo(igmediaboosteligibilityinfo_id)
    return obj.api_get(fields=fields)
