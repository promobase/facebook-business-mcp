"""BroadTargetingCategories MCP Server."""

from typing import Any

from facebook_business.adobjects.broadtargetingcategories import BroadTargetingCategories
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBroadTargetingCategories"
instructions = """
BroadTargetingCategories MCP Server for Facebook Business API.

Provides typed access to all BroadTargetingCategories operations.
"""

broadtargetingcategories_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@broadtargetingcategories_server.tool
@wrapped_fn_tool
def get_endpoint(
    broadtargetingcategories_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return BroadTargetingCategories(broadtargetingcategories_id).get_endpoint(
        fields=fields, params=params
    )
