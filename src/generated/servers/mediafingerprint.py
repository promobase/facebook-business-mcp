"""
Auto-generated MCP server for Facebook MediaFingerprint.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.mediafingerprint import MediaFingerprint
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-mediafingerprint")


# CRUD Operations


@mcp.tool()
async def get_mediafingerprint(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a MediaFingerprint.

    Args:
        object_id: The ID of the MediaFingerprint
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = MediaFingerprint(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_mediafingerprint(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a MediaFingerprint.

    Args:
        object_id: The ID of the MediaFingerprint
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = MediaFingerprint(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
mediafingerprint_server = mcp
