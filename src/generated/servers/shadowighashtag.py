"""
Auto-generated MCP server for Facebook ShadowIGHashtag.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.shadowighashtag import ShadowIGHashtag
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-shadowighashtag")


# CRUD Operations


@mcp.tool()
async def get_shadowighashtag(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ShadowIGHashtag.

    Args:
        object_id: The ID of the ShadowIGHashtag
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ShadowIGHashtag(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_recent_media_for_shadowighashtag(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Recent Media for ShadowIGHashtag.

    Args:
        object_id: The ID of the ShadowIGHashtag
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_recent_media result
    """
    result = ShadowIGHashtag(fbid=object_id).get_recent_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_top_media_for_shadowighashtag(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Top Media for ShadowIGHashtag.

    Args:
        object_id: The ID of the ShadowIGHashtag
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_top_media result
    """
    result = ShadowIGHashtag(fbid=object_id).get_top_media(
        fields=fields,
        params=params,
    )

    return result


# Export the server
shadowighashtag_server = mcp
