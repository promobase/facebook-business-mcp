"""
Auto-generated MCP server for Facebook PageBroadcast.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pagebroadcast import PageBroadcast
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-pagebroadcast")


# CRUD Operations


@mcp.tool()
async def get_pagebroadcast(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a PageBroadcast.

    Args:
        object_id: The ID of the PageBroadcast
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = PageBroadcast(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pagebroadcast_server = mcp
