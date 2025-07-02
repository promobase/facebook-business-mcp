"""AdLightCampaign MCP Server with typed wrappers."""

from facebook_business.adobjects.adlightcampaign import AdLightCampaign
from fastmcp import FastMCP

from src.generated.models.adlightcampaign import AdLightCampaignField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdLightCampaign"
instructions = """
AdLightCampaign MCP Server for Facebook Business API.

Provides typed access to all AdLightCampaign operations.
"""

adlightcampaign_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adlightcampaign_server.tool
@wrapped_fn_tool
def get_adlightcampaign(
    adlightcampaign_id: str,
    fields: list[AdLightCampaignField] = [],
) -> str:
    """Get a AdLightCampaign object by ID.

    Args:
        adlightcampaign_id: The ID of the AdLightCampaign.
        fields: Fields to retrieve. Available fields: See AdLightCampaignField type.
    """
    obj = AdLightCampaign(adlightcampaign_id)
    return obj.api_get(fields=fields)
