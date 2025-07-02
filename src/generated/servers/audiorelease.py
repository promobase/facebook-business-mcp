"""
Auto-generated MCP server for Facebook AudioRelease.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.audiorelease import AudioRelease
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-audiorelease")


# CRUD Operations


@mcp.tool()
async def get_audiorelease(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AudioRelease.

    Args:
        object_id: The ID of the AudioRelease
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AudioRelease(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
audiorelease_server = mcp
