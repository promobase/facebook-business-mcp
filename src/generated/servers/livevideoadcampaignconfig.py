"""LiveVideoAdCampaignConfig MCP Server with typed wrappers."""

from facebook_business.adobjects.livevideoadcampaignconfig import LiveVideoAdCampaignConfig
from fastmcp import FastMCP

from src.generated.models.livevideoadcampaignconfig import LiveVideoAdCampaignConfigField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLiveVideoAdCampaignConfig"
instructions = """
LiveVideoAdCampaignConfig MCP Server for Facebook Business API.

Provides typed access to all LiveVideoAdCampaignConfig operations.
"""

livevideoadcampaignconfig_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@livevideoadcampaignconfig_server.tool
@wrapped_fn_tool
def get_livevideoadcampaignconfig(
    livevideoadcampaignconfig_id: str,
    fields: list[LiveVideoAdCampaignConfigField] = [],
) -> str:
    """Get a LiveVideoAdCampaignConfig object by ID.

    Args:
        livevideoadcampaignconfig_id: The ID of the LiveVideoAdCampaignConfig.
        fields: Fields to retrieve. Available fields: See LiveVideoAdCampaignConfigField type.
    """
    obj = LiveVideoAdCampaignConfig(livevideoadcampaignconfig_id)
    return obj.api_get(fields=fields)
