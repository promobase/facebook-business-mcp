"""AdsInsights MCP Server."""

from typing import Any

from facebook_business.adobjects.adsinsights import AdsInsights
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsInsights"
instructions = """
AdsInsights MCP Server for Facebook Business API.

Provides typed access to all AdsInsights operations.
"""

adsinsights_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@adsinsights_server.tool
@wrapped_fn_tool
def get_endpoint(
    adsinsights_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdsInsights(adsinsights_id).get_endpoint(fields=fields, params=params)
