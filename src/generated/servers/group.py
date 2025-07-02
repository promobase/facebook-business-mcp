"""
Auto-generated MCP server for Facebook Group.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.group import Group
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-group")


# CRUD Operations


@mcp.tool()
async def get_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Group(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = Group(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_admin_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Admin for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_admin result
    """
    result = Group(fbid=object_id).create_admin(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_feed_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Feed for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_feed result
    """
    result = Group(fbid=object_id).create_feed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_group_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Group for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_group result
    """
    result = Group(fbid=object_id).create_group(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_live_video_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Live Video for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_live_video result
    """
    result = Group(fbid=object_id).create_live_video(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_member_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Member for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_member result
    """
    result = Group(fbid=object_id).create_member(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_photo_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Photo for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_photo result
    """
    result = Group(fbid=object_id).create_photo(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_video_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Video for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_video result
    """
    result = Group(fbid=object_id).create_video(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_admins_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Admins for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_admins result
    """
    result = Group(fbid=object_id).delete_admins(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_members_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Members for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_members result
    """
    result = Group(fbid=object_id).delete_members(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_albums_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Albums for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_albums result
    """
    result = Group(fbid=object_id).get_albums(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_docs_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Docs for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_docs result
    """
    result = Group(fbid=object_id).get_docs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_events_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Events for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_events result
    """
    result = Group(fbid=object_id).get_events(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_feed_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Feed for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_feed result
    """
    result = Group(fbid=object_id).get_feed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_files_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Files for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_files result
    """
    result = Group(fbid=object_id).get_files(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_groups_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Groups for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_groups result
    """
    result = Group(fbid=object_id).get_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_live_videos_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Live Videos for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_live_videos result
    """
    result = Group(fbid=object_id).get_live_videos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_opted_in_members_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Opted In Members for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_opted_in_members result
    """
    result = Group(fbid=object_id).get_opted_in_members(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_picture_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Picture for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_picture result
    """
    result = Group(fbid=object_id).get_picture(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_videos_for_group(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Videos for Group.

    Args:
        object_id: The ID of the Group
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_videos result
    """
    result = Group(fbid=object_id).get_videos(
        fields=fields,
        params=params,
    )

    return result


# Export the server
group_server = mcp
