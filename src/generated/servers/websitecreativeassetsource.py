"""
Auto-generated MCP server for Facebook WebsiteCreativeAssetSource.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.websitecreativeassetsource import WebsiteCreativeAssetSource
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-websitecreativeassetsource")


# CRUD Operations


@mcp.tool()
async def get_websitecreativeassetsource(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a WebsiteCreativeAssetSource.

    Args:
        object_id: The ID of the WebsiteCreativeAssetSource
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = WebsiteCreativeAssetSource(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
websitecreativeassetsource_server = mcp
