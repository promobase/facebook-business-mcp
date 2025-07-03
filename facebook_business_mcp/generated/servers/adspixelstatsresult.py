"""AdsPixelStatsResult MCP Server."""

from typing import Any

from facebook_business.adobjects.adspixelstatsresult import AdsPixelStatsResult
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsPixelStatsResult"
instructions = """
AdsPixelStatsResult MCP Server for Facebook Business API.

Provides typed access to all AdsPixelStatsResult operations.
"""

adspixelstatsresult_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@adspixelstatsresult_server.tool
@wrapped_fn_tool
def get_endpoint(
    adspixelstatsresult_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsPixelStatsResult(adspixelstatsresult_id).get_endpoint(fields=fields, params=params)
