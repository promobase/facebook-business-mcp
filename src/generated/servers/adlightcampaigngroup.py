"""
Auto-generated MCP server for Facebook AdLightCampaignGroup.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adlightcampaigngroup import AdLightCampaignGroup
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adlightcampaigngroup")


# CRUD Operations


@mcp.tool()
async def get_adlightcampaigngroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdLightCampaignGroup.

    Args:
        object_id: The ID of the AdLightCampaignGroup
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdLightCampaignGroup(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adlightcampaigngroup_server = mcp
