"""
Auto-generated MCP server for Facebook AvatarProfilePicture.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.avatarprofilepicture import AvatarProfilePicture
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-avatarprofilepicture")


# CRUD Operations


@mcp.tool()
async def get_avatarprofilepicture(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AvatarProfilePicture.

    Args:
        object_id: The ID of the AvatarProfilePicture
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AvatarProfilePicture(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
avatarprofilepicture_server = mcp
