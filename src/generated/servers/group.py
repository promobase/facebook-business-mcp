"""Group MCP Server with typed wrappers."""

from facebook_business.adobjects.group import Group
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.advideo import AdVideoField
from src.generated.models.group import (
    GroupCreateAdminParams,
    GroupCreateFeedParams,
    GroupCreateGroupParams,
    GroupCreateLiveVideoParams,
    GroupCreateMemberParams,
    GroupCreatePhotoParams,
    GroupCreateVideoParams,
    GroupDeleteAdminsParams,
    GroupDeleteMembersParams,
    GroupField,
    GroupGetFeedParams,
    GroupGetLiveVideosParams,
    GroupGetPictureParams,
    GroupGetVideosParams,
    GroupUpdateParams,
)
from src.generated.models.livevideo import LiveVideoField
from src.generated.models.photo import PhotoField
from src.generated.models.post import PostField
from src.generated.models.profilepicturesource import ProfilePictureSourceField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookGroup"
instructions = """
Group MCP Server for Facebook Business API.

Provides typed access to all Group operations.
"""

group_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@group_server.tool
@wrapped_fn_tool
def get_group(
    group_id: str,
    fields: list[GroupField] = [],
) -> str:
    """Get a Group object by ID.

    Args:
        group_id: The ID of the Group.
        fields: Fields to retrieve. Available fields: See GroupField type.
    """
    obj = Group(group_id)
    return obj.api_get(fields=fields)


@group_server.tool
@wrapped_fn_tool
def update_group(
    group_id: str,
    fields: list[GroupField] = [],
    params: GroupUpdateParams | dict = {},
) -> str:
    """Update a Group object.

    Args:
        group_id: The ID of the Group.
        fields: Fields to return after update. Available fields: See GroupField type.
        params: Parameters to update. Available params: See GroupUpdateParams type.
    """
    return Group(group_id).api_update(fields=fields, params=params)


# ---- Edge Methods (13) ----
@group_server.tool
@wrapped_fn_tool
def delete_admins(
    group_id: str,
    params: GroupDeleteAdminsParams | dict = {},
):
    """Delete Admins for this Group.

    Args:
        group_id: The ID of the Group.
        params: Query parameters. Available params: See GroupDeleteAdminsParams type.
    """
    return Group(group_id).delete_admins(params=params)


@group_server.tool
@wrapped_fn_tool
def create_admin(
    group_id: str,
    fields: list[str] = [],
    params: GroupCreateAdminParams | dict = {},
):
    """Create Admin for this Group.

    Args:
        group_id: The ID of the Group.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See GroupCreateAdminParams type.
    """
    return Group(group_id).create_admin(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def get_feed(
    group_id: str,
    fields: list[PostField] = [],
    params: GroupGetFeedParams | dict = {},
):
    """Get Feed for this Group.

    Args:
        group_id: The ID of the Group.
        fields: Fields to retrieve. Available fields: See PostField type.
        params: Query parameters. Available params: See GroupGetFeedParams type.
    """
    return Group(group_id).get_feed(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def create_feed(
    group_id: str,
    fields: list[str] = [],
    params: GroupCreateFeedParams | dict = {},
):
    """Create Feed for this Group.

    Args:
        group_id: The ID of the Group.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See GroupCreateFeedParams type.
    """
    return Group(group_id).create_feed(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def create_group(
    group_id: str,
    fields: list[str] = [],
    params: GroupCreateGroupParams | dict = {},
):
    """Create Group for this Group.

    Args:
        group_id: The ID of the Group.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See GroupCreateGroupParams type.
    """
    return Group(group_id).create_group(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def get_live_videos(
    group_id: str,
    fields: list[LiveVideoField] = [],
    params: GroupGetLiveVideosParams | dict = {},
):
    """Get Live Videos for this Group.

    Args:
        group_id: The ID of the Group.
        fields: Fields to retrieve. Available fields: See LiveVideoField type.
        params: Query parameters. Available params: See GroupGetLiveVideosParams type.
    """
    return Group(group_id).get_live_videos(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def create_live_video(
    group_id: str,
    fields: list[str] = [],
    params: GroupCreateLiveVideoParams | dict = {},
):
    """Create Live Video for this Group.

    Args:
        group_id: The ID of the Group.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See GroupCreateLiveVideoParams type.
    """
    return Group(group_id).create_live_video(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def delete_members(
    group_id: str,
    params: GroupDeleteMembersParams | dict = {},
):
    """Delete Members for this Group.

    Args:
        group_id: The ID of the Group.
        params: Query parameters. Available params: See GroupDeleteMembersParams type.
    """
    return Group(group_id).delete_members(params=params)


@group_server.tool
@wrapped_fn_tool
def create_member(
    group_id: str,
    fields: list[str] = [],
    params: GroupCreateMemberParams | dict = {},
):
    """Create Member for this Group.

    Args:
        group_id: The ID of the Group.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See GroupCreateMemberParams type.
    """
    return Group(group_id).create_member(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def create_photo(
    group_id: str,
    fields: list[str] = [],
    params: GroupCreatePhotoParams | dict = {},
):
    """Create Photo for this Group.

    Args:
        group_id: The ID of the Group.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See GroupCreatePhotoParams type.
    """
    return Group(group_id).create_photo(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def get_picture(
    group_id: str,
    fields: list[ProfilePictureSourceField] = [],
    params: GroupGetPictureParams | dict = {},
):
    """Get Picture for this Group.

    Args:
        group_id: The ID of the Group.
        fields: Fields to retrieve. Available fields: See ProfilePictureSourceField type.
        params: Query parameters. Available params: See GroupGetPictureParams type.
    """
    return Group(group_id).get_picture(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def get_videos(
    group_id: str,
    fields: list[AdVideoField] = [],
    params: GroupGetVideosParams | dict = {},
):
    """Get Videos for this Group.

    Args:
        group_id: The ID of the Group.
        fields: Fields to retrieve. Available fields: See AdVideoField type.
        params: Query parameters. Available params: See GroupGetVideosParams type.
    """
    return Group(group_id).get_videos(fields=fields, params=params)


@group_server.tool
@wrapped_fn_tool
def create_video(
    group_id: str,
    fields: list[str] = [],
    params: GroupCreateVideoParams | dict = {},
):
    """Create Video for this Group.

    Args:
        group_id: The ID of the Group.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See GroupCreateVideoParams type.
    """
    return Group(group_id).create_video(fields=fields, params=params)
