"""
Auto-generated MCP server for Facebook Avatar.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.avatar import Avatar
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-avatar")


# CRUD Operations


@mcp.tool()
async def get_avatar(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Avatar.

    Args:
        object_id: The ID of the Avatar
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Avatar(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_models_for_avatar(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Models for Avatar.

    Args:
        object_id: The ID of the Avatar
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_models result
    """
    result = Avatar(fbid=object_id).get_models(
        fields=fields,
        params=params,
    )

    return result


# Export the server
avatar_server = mcp
