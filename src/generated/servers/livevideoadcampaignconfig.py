"""
Auto-generated MCP server for Facebook LiveVideoAdCampaignConfig.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.livevideoadcampaignconfig import LiveVideoAdCampaignConfig
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-livevideoadcampaignconfig")


# CRUD Operations


@mcp.tool()
async def get_livevideoadcampaignconfig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a LiveVideoAdCampaignConfig.

    Args:
        object_id: The ID of the LiveVideoAdCampaignConfig
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = LiveVideoAdCampaignConfig(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
livevideoadcampaignconfig_server = mcp
