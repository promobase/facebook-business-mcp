"""
Auto-generated MCP server for Facebook PublisherWhiteList.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.publisherwhitelist import PublisherWhiteList
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-publisherwhitelist")


# CRUD Operations


@mcp.tool()
async def get_publisherwhitelist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a PublisherWhiteList.

    Args:
        object_id: The ID of the PublisherWhiteList
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = PublisherWhiteList(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
publisherwhitelist_server = mcp
