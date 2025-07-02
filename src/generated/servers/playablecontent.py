"""
Auto-generated MCP server for Facebook PlayableContent.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.playablecontent import PlayableContent
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-playablecontent")


# CRUD Operations


@mcp.tool()
async def create_playablecontent(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a PlayableContent.

    Args:
        object_id: The ID of the PlayableContent
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = PlayableContent(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_playablecontent(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a PlayableContent.

    Args:
        object_id: The ID of the PlayableContent
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = PlayableContent(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
playablecontent_server = mcp
