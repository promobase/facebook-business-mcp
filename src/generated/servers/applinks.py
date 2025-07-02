"""
Auto-generated MCP server for Facebook AppLinks.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.applinks import AppLinks
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-applinks")


# CRUD Operations


@mcp.tool()
async def get_applinks(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AppLinks.

    Args:
        object_id: The ID of the AppLinks
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AppLinks(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
applinks_server = mcp
