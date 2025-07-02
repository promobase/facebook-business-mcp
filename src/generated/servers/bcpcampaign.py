"""BCPCampaign MCP Server with typed wrappers."""

from facebook_business.adobjects.bcpcampaign import BCPCampaign
from fastmcp import FastMCP

from src.generated.models.bcpcampaign import BCPCampaignField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBCPCampaign"
instructions = """
BCPCampaign MCP Server for Facebook Business API.

Provides typed access to all BCPCampaign operations.
"""

bcpcampaign_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@bcpcampaign_server.tool
@wrapped_fn_tool
def get_bcpcampaign(
    bcpcampaign_id: str,
    fields: list[BCPCampaignField] = [],
) -> str:
    """Get a BCPCampaign object by ID.

    Args:
        bcpcampaign_id: The ID of the BCPCampaign.
        fields: Fields to retrieve. Available fields: See BCPCampaignField type.
    """
    obj = BCPCampaign(bcpcampaign_id)
    return obj.api_get(fields=fields)
