"""
Auto-generated MCP server for Facebook Place.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.place import Place
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-place")


# CRUD Operations


@mcp.tool()
async def get_place(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Place.

    Args:
        object_id: The ID of the Place
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Place(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
place_server = mcp
