"""
Auto-generated MCP server for Facebook LiveVideoError.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.livevideoerror import LiveVideoError
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-livevideoerror")


# CRUD Operations


@mcp.tool()
async def get_livevideoerror(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a LiveVideoError.

    Args:
        object_id: The ID of the LiveVideoError
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = LiveVideoError(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
livevideoerror_server = mcp
