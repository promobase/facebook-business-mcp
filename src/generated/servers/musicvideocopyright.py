"""
Auto-generated MCP server for Facebook MusicVideoCopyright.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.musicvideocopyright import MusicVideoCopyright
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-musicvideocopyright")


# CRUD Operations


@mcp.tool()
async def get_musicvideocopyright(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a MusicVideoCopyright.

    Args:
        object_id: The ID of the MusicVideoCopyright
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = MusicVideoCopyright(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
musicvideocopyright_server = mcp
