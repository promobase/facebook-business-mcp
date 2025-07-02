"""
Auto-generated MCP server for Facebook AudioAsset.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.audioasset import AudioAsset
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-audioasset")


# CRUD Operations


@mcp.tool()
async def get_audioasset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AudioAsset.

    Args:
        object_id: The ID of the AudioAsset
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AudioAsset(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
audioasset_server = mcp
