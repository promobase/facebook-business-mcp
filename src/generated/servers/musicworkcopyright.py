"""
Auto-generated MCP server for Facebook MusicWorkCopyright.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.musicworkcopyright import MusicWorkCopyright
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-musicworkcopyright")


# CRUD Operations


@mcp.tool()
async def get_musicworkcopyright(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a MusicWorkCopyright.

    Args:
        object_id: The ID of the MusicWorkCopyright
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = MusicWorkCopyright(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
musicworkcopyright_server = mcp
