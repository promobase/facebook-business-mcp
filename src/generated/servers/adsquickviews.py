"""AdsQuickViews MCP Server."""

from typing import Any

from facebook_business.adobjects.adsquickviews import AdsQuickViews
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsQuickViews"
instructions = """
AdsQuickViews MCP Server for Facebook Business API.

Provides typed access to all AdsQuickViews operations.
"""

adsquickviews_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adsquickviews_server.tool
@wrapped_fn_tool
def get_adsquickviews(
    adsquickviews_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdsQuickViews(adsquickviews_id)
    return obj.api_get(fields=fields)
