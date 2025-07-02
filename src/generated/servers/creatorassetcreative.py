"""
Auto-generated MCP server for Facebook CreatorAssetCreative.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.creatorassetcreative import CreatorAssetCreative
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-creatorassetcreative")


# CRUD Operations


@mcp.tool()
async def get_creatorassetcreative(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CreatorAssetCreative.

    Args:
        object_id: The ID of the CreatorAssetCreative
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CreatorAssetCreative(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
creatorassetcreative_server = mcp
