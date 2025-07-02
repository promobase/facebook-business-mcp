"""
Auto-generated MCP server for Facebook ManagementSiteLink.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.managementsitelink import ManagementSiteLink
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-managementsitelink")


# CRUD Operations


@mcp.tool()
async def get_managementsitelink(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ManagementSiteLink.

    Args:
        object_id: The ID of the ManagementSiteLink
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ManagementSiteLink(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
managementsitelink_server = mcp
