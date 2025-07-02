"""AdsUserSettings MCP Server."""

from typing import Any

from facebook_business.adobjects.adsusersettings import AdsUserSettings
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsUserSettings"
instructions = """
AdsUserSettings MCP Server for Facebook Business API.

Provides typed access to all AdsUserSettings operations.
"""

adsusersettings_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adsusersettings_server.tool
@wrapped_fn_tool
def get_adsusersettings(
    adsusersettings_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdsUserSettings(adsusersettings_id)
    return obj.api_get(fields=fields)
