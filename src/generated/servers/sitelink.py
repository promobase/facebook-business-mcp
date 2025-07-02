"""
Auto-generated MCP server for Facebook SiteLink.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.sitelink import SiteLink
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-sitelink")


# CRUD Operations


@mcp.tool()
async def get_sitelink(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a SiteLink.

    Args:
        object_id: The ID of the SiteLink
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = SiteLink(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
sitelink_server = mcp
