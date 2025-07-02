"""AdsConversionGoal MCP Server."""

from typing import Any

from facebook_business.adobjects.adsconversiongoal import AdsConversionGoal
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsConversionGoal"
instructions = """
AdsConversionGoal MCP Server for Facebook Business API.

Provides typed access to all AdsConversionGoal operations.
"""

adsconversiongoal_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adsconversiongoal_server.tool
@wrapped_fn_tool
def get_adsconversiongoal(
    adsconversiongoal_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdsConversionGoal(adsconversiongoal_id)
    return obj.api_get(fields=fields)
