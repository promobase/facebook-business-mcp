"""
Auto-generated MCP server for Facebook AdImage.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adimage import AdImage
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adimage")


# CRUD Operations


@mcp.tool()
async def create_adimage(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a AdImage.

    Args:
        object_id: The ID of the AdImage
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = AdImage(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adimage(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdImage.

    Args:
        object_id: The ID of the AdImage
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdImage(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adimage_server = mcp
