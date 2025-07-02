"""
Auto-generated MCP server for Facebook BCPCampaign.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.bcpcampaign import BCPCampaign
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-bcpcampaign")


# CRUD Operations


@mcp.tool()
async def get_bcpcampaign(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BCPCampaign.

    Args:
        object_id: The ID of the BCPCampaign
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BCPCampaign(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
bcpcampaign_server = mcp
