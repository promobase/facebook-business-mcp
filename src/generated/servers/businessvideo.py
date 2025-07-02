"""
Auto-generated MCP server for Facebook BusinessVideo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessvideo import BusinessVideo
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessvideo")


# CRUD Operations


@mcp.tool()
async def get_businessvideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BusinessVideo.

    Args:
        object_id: The ID of the BusinessVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BusinessVideo(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessvideo_server = mcp
