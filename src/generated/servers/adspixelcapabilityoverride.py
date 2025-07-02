"""AdsPixelCapabilityOverride MCP Server."""

from typing import Any

from facebook_business.adobjects.adspixelcapabilityoverride import AdsPixelCapabilityOverride
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsPixelCapabilityOverride"
instructions = """
AdsPixelCapabilityOverride MCP Server for Facebook Business API.

Provides typed access to all AdsPixelCapabilityOverride operations.
"""

adspixelcapabilityoverride_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adspixelcapabilityoverride_server.tool
@wrapped_fn_tool
def get_adspixelcapabilityoverride(
    adspixelcapabilityoverride_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdsPixelCapabilityOverride(adspixelcapabilityoverride_id)
    return obj.api_get(fields=fields)
