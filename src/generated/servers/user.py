"""User MCP Server with typed wrappers."""

from facebook_business.adobjects.user import User
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.adstudy import AdStudyField
from src.generated.models.advideo import AdVideoField
from src.generated.models.business import BusinessField
from src.generated.models.businessassetgroup import BusinessAssetGroupField
from src.generated.models.canvas import CanvasField
from src.generated.models.event import EventField
from src.generated.models.fundraiserpersontocharity import FundraiserPersonToCharityField
from src.generated.models.group import GroupField
from src.generated.models.livevideo import LiveVideoField
from src.generated.models.page import PageField
from src.generated.models.permission import PermissionField
from src.generated.models.photo import PhotoField
from src.generated.models.post import PostField
from src.generated.models.profilepicturesource import ProfilePictureSourceField
from src.generated.models.unifiedthread import UnifiedThreadField
from src.generated.models.user import (
    UserCreateAccessTokenParams,
    UserCreateAccountParams,
    UserCreateAdStudyParams,
    UserCreateApplicationParams,
    UserCreateBusinessParams,
    UserCreateFeedParams,
    UserCreateFundraiserParams,
    UserCreateLiveVideoParams,
    UserCreateMessengerKidsAccountsUnreadBadgeParams,
    UserCreateNotificationParams,
    UserCreatePhotoParams,
    UserCreateStagingResourceParams,
    UserCreateVideoParams,
    UserDeleteBusinessesParams,
    UserDeletePermissionsParams,
    UserField,
    UserGetAccountsParams,
    UserGetAssignedBusinessAssetGroupsParams,
    UserGetAssignedPagesParams,
    UserGetConversationsParams,
    UserGetEventsParams,
    UserGetFeedParams,
    UserGetFriendsParams,
    UserGetGroupsParams,
    UserGetIdsForAppsParams,
    UserGetIdsForBusinessParams,
    UserGetIdsForPagesParams,
    UserGetLikesParams,
    UserGetLiveVideosParams,
    UserGetMusicParams,
    UserGetPermissionsParams,
    UserGetPhotosParams,
    UserGetPictureParams,
    UserGetPostsParams,
    UserGetRichMediaDocumentsParams,
    UserGetVideosParams,
    UserUpdateParams,
)
from src.generated.models.useridforapp import UserIDForAppField
from src.generated.models.useridforpage import UserIDForPageField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookUser"
instructions = """
User MCP Server for Facebook Business API.

Provides typed access to all User operations.
"""

user_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@user_server.tool
@wrapped_fn_tool
def get_user(
    user_id: str,
    fields: list[UserField] = [],
) -> str:
    """Get a User object by ID.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See UserField type.
    """
    obj = User(user_id)
    return obj.api_get(fields=fields)


@user_server.tool
@wrapped_fn_tool
def update_user(
    user_id: str,
    fields: list[UserField] = [],
    params: UserUpdateParams | dict = {},
) -> str:
    """Update a User object.

    Args:
        user_id: The ID of the User.
        fields: Fields to return after update. Available fields: See UserField type.
        params: Parameters to update. Available params: See UserUpdateParams type.
    """
    return User(user_id).api_update(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def delete_user(
    user_id: str,
) -> str:
    """Delete a User object.

    Args:
        user_id: The ID of the User.
    """
    return User(user_id).api_delete()


# ---- Edge Methods (35) ----
@user_server.tool
@wrapped_fn_tool
def create_access_token(
    user_id: str,
    fields: list[str] = [],
    params: UserCreateAccessTokenParams | dict = {},
):
    """Create Access Token for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See UserCreateAccessTokenParams type.
    """
    return User(user_id).create_access_token(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_accounts(
    user_id: str,
    fields: list[PageField] = [],
    params: UserGetAccountsParams | dict = {},
):
    """Get Accounts for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See PageField type.
        params: Query parameters. Available params: See UserGetAccountsParams type.
    """
    return User(user_id).get_accounts(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_account(
    user_id: str,
    fields: list[str] = [],
    params: UserCreateAccountParams | dict = {},
):
    """Create Account for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See UserCreateAccountParams type.
    """
    return User(user_id).create_account(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_ad_study(
    user_id: str,
    fields: list[str] = [],
    params: UserCreateAdStudyParams | dict = {},
):
    """Create Ad Study for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See UserCreateAdStudyParams type.
    """
    return User(user_id).create_ad_study(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_application(
    user_id: str,
    fields: list[str] = [],
    params: UserCreateApplicationParams | dict = {},
):
    """Create Application for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See UserCreateApplicationParams type.
    """
    return User(user_id).create_application(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_assigned_business_asset_groups(
    user_id: str,
    fields: list[BusinessAssetGroupField] = [],
    params: UserGetAssignedBusinessAssetGroupsParams | dict = {},
):
    """Get Assigned Business Asset Groups for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See BusinessAssetGroupField type.
        params: Query parameters. Available params: See UserGetAssignedBusinessAssetGroupsParams type.
    """
    return User(user_id).get_assigned_business_asset_groups(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_assigned_pages(
    user_id: str,
    fields: list[PageField] = [],
    params: UserGetAssignedPagesParams | dict = {},
):
    """Get Assigned Pages for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See PageField type.
        params: Query parameters. Available params: See UserGetAssignedPagesParams type.
    """
    return User(user_id).get_assigned_pages(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def delete_businesses(
    user_id: str,
    params: UserDeleteBusinessesParams | dict = {},
):
    """Delete Businesses for this User.

    Args:
        user_id: The ID of the User.
        params: Query parameters. Available params: See UserDeleteBusinessesParams type.
    """
    return User(user_id).delete_businesses(params=params)


@user_server.tool
@wrapped_fn_tool
def create_business(
    user_id: str,
    fields: list[str] = [],
    params: UserCreateBusinessParams | dict = {},
):
    """Create Business for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See UserCreateBusinessParams type.
    """
    return User(user_id).create_business(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_conversations(
    user_id: str,
    fields: list[UnifiedThreadField] = [],
    params: UserGetConversationsParams | dict = {},
):
    """Get Conversations for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See UnifiedThreadField type.
        params: Query parameters. Available params: See UserGetConversationsParams type.
    """
    return User(user_id).get_conversations(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_events(
    user_id: str,
    fields: list[EventField] = [],
    params: UserGetEventsParams | dict = {},
):
    """Get Events for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See EventField type.
        params: Query parameters. Available params: See UserGetEventsParams type.
    """
    return User(user_id).get_events(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_feed(
    user_id: str,
    fields: list[PostField] = [],
    params: UserGetFeedParams | dict = {},
):
    """Get Feed for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See PostField type.
        params: Query parameters. Available params: See UserGetFeedParams type.
    """
    return User(user_id).get_feed(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_feed(
    user_id: str,
    fields: list[str] = [],
    params: UserCreateFeedParams | dict = {},
):
    """Create Feed for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See UserCreateFeedParams type.
    """
    return User(user_id).create_feed(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_friends(
    user_id: str,
    fields: list[UserField] = [],
    params: UserGetFriendsParams | dict = {},
):
    """Get Friends for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See UserField type.
        params: Query parameters. Available params: See UserGetFriendsParams type.
    """
    return User(user_id).get_friends(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_fundraiser(
    user_id: str,
    fields: list[str] = [],
    params: UserCreateFundraiserParams | dict = {},
):
    """Create Fundraiser for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See UserCreateFundraiserParams type.
    """
    return User(user_id).create_fundraiser(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_groups(
    user_id: str,
    fields: list[GroupField] = [],
    params: UserGetGroupsParams | dict = {},
):
    """Get Groups for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See GroupField type.
        params: Query parameters. Available params: See UserGetGroupsParams type.
    """
    return User(user_id).get_groups(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_ids_for_apps(
    user_id: str,
    fields: list[UserIDForAppField] = [],
    params: UserGetIdsForAppsParams | dict = {},
):
    """Get Ids For Apps for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See UserIDForAppField type.
        params: Query parameters. Available params: See UserGetIdsForAppsParams type.
    """
    return User(user_id).get_ids_for_apps(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_ids_for_business(
    user_id: str,
    fields: list[UserIDForAppField] = [],
    params: UserGetIdsForBusinessParams | dict = {},
):
    """Get Ids For Business for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See UserIDForAppField type.
        params: Query parameters. Available params: See UserGetIdsForBusinessParams type.
    """
    return User(user_id).get_ids_for_business(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_ids_for_pages(
    user_id: str,
    fields: list[UserIDForPageField] = [],
    params: UserGetIdsForPagesParams | dict = {},
):
    """Get Ids For Pages for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See UserIDForPageField type.
        params: Query parameters. Available params: See UserGetIdsForPagesParams type.
    """
    return User(user_id).get_ids_for_pages(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_likes(
    user_id: str,
    fields: list[PageField] = [],
    params: UserGetLikesParams | dict = {},
):
    """Get Likes for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See PageField type.
        params: Query parameters. Available params: See UserGetLikesParams type.
    """
    return User(user_id).get_likes(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_live_videos(
    user_id: str,
    fields: list[LiveVideoField] = [],
    params: UserGetLiveVideosParams | dict = {},
):
    """Get Live Videos for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See LiveVideoField type.
        params: Query parameters. Available params: See UserGetLiveVideosParams type.
    """
    return User(user_id).get_live_videos(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_live_video(
    user_id: str,
    fields: list[str] = [],
    params: UserCreateLiveVideoParams | dict = {},
):
    """Create Live Video for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See UserCreateLiveVideoParams type.
    """
    return User(user_id).create_live_video(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_messenger_kids_accounts_unread_badge(
    user_id: str,
    fields: list[str] = [],
    params: UserCreateMessengerKidsAccountsUnreadBadgeParams | dict = {},
):
    """Create Messenger Kids Accounts Unread Badge for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See UserCreateMessengerKidsAccountsUnreadBadgeParams type.
    """
    return User(user_id).create_messenger_kids_accounts_unread_badge(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_music(
    user_id: str,
    fields: list[PageField] = [],
    params: UserGetMusicParams | dict = {},
):
    """Get Music for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See PageField type.
        params: Query parameters. Available params: See UserGetMusicParams type.
    """
    return User(user_id).get_music(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_notification(
    user_id: str,
    fields: list[str] = [],
    params: UserCreateNotificationParams | dict = {},
):
    """Create Notification for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See UserCreateNotificationParams type.
    """
    return User(user_id).create_notification(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def delete_permissions(
    user_id: str,
    params: UserDeletePermissionsParams | dict = {},
):
    """Delete Permissions for this User.

    Args:
        user_id: The ID of the User.
        params: Query parameters. Available params: See UserDeletePermissionsParams type.
    """
    return User(user_id).delete_permissions(params=params)


@user_server.tool
@wrapped_fn_tool
def get_permissions(
    user_id: str,
    fields: list[PermissionField] = [],
    params: UserGetPermissionsParams | dict = {},
):
    """Get Permissions for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See PermissionField type.
        params: Query parameters. Available params: See UserGetPermissionsParams type.
    """
    return User(user_id).get_permissions(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_photos(
    user_id: str,
    fields: list[PhotoField] = [],
    params: UserGetPhotosParams | dict = {},
):
    """Get Photos for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See PhotoField type.
        params: Query parameters. Available params: See UserGetPhotosParams type.
    """
    return User(user_id).get_photos(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_photo(
    user_id: str,
    fields: list[str] = [],
    params: UserCreatePhotoParams | dict = {},
):
    """Create Photo for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See UserCreatePhotoParams type.
    """
    return User(user_id).create_photo(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_picture(
    user_id: str,
    fields: list[ProfilePictureSourceField] = [],
    params: UserGetPictureParams | dict = {},
):
    """Get Picture for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See ProfilePictureSourceField type.
        params: Query parameters. Available params: See UserGetPictureParams type.
    """
    return User(user_id).get_picture(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_posts(
    user_id: str,
    fields: list[PostField] = [],
    params: UserGetPostsParams | dict = {},
):
    """Get Posts for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See PostField type.
        params: Query parameters. Available params: See UserGetPostsParams type.
    """
    return User(user_id).get_posts(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_rich_media_documents(
    user_id: str,
    fields: list[CanvasField] = [],
    params: UserGetRichMediaDocumentsParams | dict = {},
):
    """Get Rich Media Documents for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See CanvasField type.
        params: Query parameters. Available params: See UserGetRichMediaDocumentsParams type.
    """
    return User(user_id).get_rich_media_documents(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_staging_resource(
    user_id: str,
    fields: list[str] = [],
    params: UserCreateStagingResourceParams | dict = {},
):
    """Create Staging Resource for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See UserCreateStagingResourceParams type.
    """
    return User(user_id).create_staging_resource(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_videos(
    user_id: str,
    fields: list[AdVideoField] = [],
    params: UserGetVideosParams | dict = {},
):
    """Get Videos for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve. Available fields: See AdVideoField type.
        params: Query parameters. Available params: See UserGetVideosParams type.
    """
    return User(user_id).get_videos(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_video(
    user_id: str,
    fields: list[str] = [],
    params: UserCreateVideoParams | dict = {},
):
    """Create Video for this User.

    Args:
        user_id: The ID of the User.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See UserCreateVideoParams type.
    """
    return User(user_id).create_video(fields=fields, params=params)
