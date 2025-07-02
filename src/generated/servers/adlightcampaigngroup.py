"""AdLightCampaignGroup MCP Server with typed wrappers."""

from facebook_business.adobjects.adlightcampaigngroup import AdLightCampaignGroup
from fastmcp import FastMCP

from src.generated.models.adlightcampaigngroup import AdLightCampaignGroupField
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
    fields: list[AdLightCampaignGroupField] = [],
) -> str:
    """Get a AdLightCampaignGroup object by ID.

    Args:
        adlightcampaigngroup_id: The ID of the AdLightCampaignGroup.
        fields: Fields to retrieve. Available fields: See AdLightCampaignGroupField type.
    """
    obj = AdLightCampaignGroup(adlightcampaigngroup_id)
    return obj.api_get(fields=fields)
