"""
Auto-generated MCP server for Facebook WebsiteCreativeInfo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.websitecreativeinfo import WebsiteCreativeInfo
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-websitecreativeinfo")


# CRUD Operations


@mcp.tool()
async def get_websitecreativeinfo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a WebsiteCreativeInfo.

    Args:
        object_id: The ID of the WebsiteCreativeInfo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = WebsiteCreativeInfo(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
websitecreativeinfo_server = mcp
