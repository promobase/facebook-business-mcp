"""
Auto-generated MCP server for Facebook URL.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.url import URL
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-url")


# CRUD Operations


@mcp.tool()
async def get_url(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a URL.

    Args:
        object_id: The ID of the URL
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = URL(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_url(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a URL.

    Args:
        object_id: The ID of the URL
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = URL(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
url_server = mcp
