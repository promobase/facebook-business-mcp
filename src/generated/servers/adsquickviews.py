"""
Auto-generated MCP server for Facebook AdsQuickViews.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsquickviews import AdsQuickViews
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsquickviews")


# CRUD Operations


@mcp.tool()
async def get_adsquickviews(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdsQuickViews.

    Args:
        object_id: The ID of the AdsQuickViews
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdsQuickViews(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsquickviews_server = mcp
