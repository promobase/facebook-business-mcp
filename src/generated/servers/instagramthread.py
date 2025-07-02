"""
Auto-generated MCP server for Facebook InstagramThread.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.instagramthread import InstagramThread
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-instagramthread")


# CRUD Operations


@mcp.tool()
async def get_instagramthread(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a InstagramThread.

    Args:
        object_id: The ID of the InstagramThread
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = InstagramThread(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
instagramthread_server = mcp
