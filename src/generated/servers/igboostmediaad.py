"""
Auto-generated MCP server for Facebook IGBoostMediaAd.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igboostmediaad import IGBoostMediaAd
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-igboostmediaad")


# CRUD Operations


@mcp.tool()
async def get_igboostmediaad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a IGBoostMediaAd.

    Args:
        object_id: The ID of the IGBoostMediaAd
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = IGBoostMediaAd(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igboostmediaad_server = mcp
