"""
Auto-generated MCP server for Facebook AdSavedKeywords.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsavedkeywords import AdSavedKeywords
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsavedkeywords")


# CRUD Operations


@mcp.tool()
async def get_adsavedkeywords(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdSavedKeywords.

    Args:
        object_id: The ID of the AdSavedKeywords
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdSavedKeywords(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsavedkeywords_server = mcp
