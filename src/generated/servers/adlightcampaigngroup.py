"""AdLightCampaignGroup MCP Server."""

from typing import Any

from facebook_business.adobjects.adlightcampaigngroup import AdLightCampaignGroup
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdLightCampaignGroup"
instructions = """
AdLightCampaignGroup MCP Server for Facebook Business API.

Provides typed access to all AdLightCampaignGroup operations.
"""

adlightcampaigngroup_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adlightcampaigngroup_server.tool
@wrapped_fn_tool
def get_adlightcampaigngroup(
    adlightcampaigngroup_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdLightCampaignGroup(adlightcampaigngroup_id)
    return obj.api_get(fields=fields)
