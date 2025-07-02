"""AdsPixelCapabilityOverride MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adspixelcapabilityoverride import AdsPixelCapabilityOverride
from fastmcp import FastMCP

from src.generated.models.adspixelcapabilityoverride import AdsPixelCapabilityOverrideField
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
    fields: list[AdsPixelCapabilityOverrideField] = [],
) -> str:
    """Get a AdsPixelCapabilityOverride object by ID.

    Args:
        adspixelcapabilityoverride_id: The ID of the AdsPixelCapabilityOverride.
        fields: Fields to retrieve. Available fields: See AdsPixelCapabilityOverrideField type.
    """
    obj = AdsPixelCapabilityOverride(adspixelcapabilityoverride_id)
    return obj.api_get(fields=fields)
