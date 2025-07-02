"""
Auto-generated MCP server for Facebook AvatarProfilePicture.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.avatarprofilepicture import AvatarProfilePicture
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-avatarprofilepicture")


# CRUD Operations


@mcp.tool()
async def api_create_avatarprofilepicture(
    avatarprofilepicture_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AvatarProfilePicture(fbid=avatarprofilepicture_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_avatarprofilepicture(
    avatarprofilepicture_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AvatarProfilePicture(fbid=avatarprofilepicture_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_avatarprofilepicture(
    avatarprofilepicture_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AvatarProfilePicture(fbid=avatarprofilepicture_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_avatarprofilepicture(
    avatarprofilepicture_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AvatarProfilePicture(fbid=avatarprofilepicture_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
avatarprofilepicture_server = mcp
