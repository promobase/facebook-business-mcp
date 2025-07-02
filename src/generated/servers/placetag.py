"""
Auto-generated MCP server for Facebook PlaceTag.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.placetag import PlaceTag
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-placetag")


# CRUD Operations


@mcp.tool()
async def get_placetag(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a PlaceTag.

    Args:
        object_id: The ID of the PlaceTag
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = PlaceTag(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
placetag_server = mcp
