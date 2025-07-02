"""
Auto-generated MCP server for Facebook Profile.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.profile import Profile
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-profile")


# CRUD Operations


@mcp.tool()
async def get_profile(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Profile.

    Args:
        object_id: The ID of the Profile
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Profile(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_picture_for_profile(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Picture for Profile.

    Args:
        object_id: The ID of the Profile
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_picture result
    """
    result = Profile(fbid=object_id).get_picture(
        fields=fields,
        params=params,
    )

    return result


# Export the server
profile_server = mcp
