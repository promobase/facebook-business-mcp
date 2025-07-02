"""
Auto-generated MCP server for Facebook User.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.user import User
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-user")


# CRUD Operations


@mcp.tool()
async def delete_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = User(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = User(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = User(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_access_token_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Access Token for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_access_token result
    """
    result = User(fbid=object_id).create_access_token(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_account_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Account for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_account result
    """
    result = User(fbid=object_id).create_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ad_study_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ad Study for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_study result
    """
    result = User(fbid=object_id).create_ad_study(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_application_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Application for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_application result
    """
    result = User(fbid=object_id).create_application(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_business_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Business for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_business result
    """
    result = User(fbid=object_id).create_business(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_feed_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Feed for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_feed result
    """
    result = User(fbid=object_id).create_feed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_fundraiser_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Fundraiser for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_fundraiser result
    """
    result = User(fbid=object_id).create_fundraiser(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_live_video_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Live Video for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_live_video result
    """
    result = User(fbid=object_id).create_live_video(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_messenger_desktop_performance_trace_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Messenger Desktop Performance Trace for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_messenger_desktop_performance_trace result
    """
    result = User(fbid=object_id).create_messenger_desktop_performance_trace(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_messenger_kids_accounts_unread_badge_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Messenger Kids Accounts Unread Badge for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_messenger_kids_accounts_unread_badge result
    """
    result = User(fbid=object_id).create_messenger_kids_accounts_unread_badge(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_notification_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Notification for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_notification result
    """
    result = User(fbid=object_id).create_notification(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_photo_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Photo for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_photo result
    """
    result = User(fbid=object_id).create_photo(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_staging_resource_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Staging Resource for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_staging_resource result
    """
    result = User(fbid=object_id).create_staging_resource(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_video_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Video for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_video result
    """
    result = User(fbid=object_id).create_video(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_access_tokens_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Access Tokens for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_access_tokens result
    """
    result = User(fbid=object_id).delete_access_tokens(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_businesses_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Businesses for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_businesses result
    """
    result = User(fbid=object_id).delete_businesses(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_permissions_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Permissions for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_permissions result
    """
    result = User(fbid=object_id).delete_permissions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_accounts_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Accounts for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_accounts result
    """
    result = User(fbid=object_id).get_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_accounts_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Accounts for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_accounts result
    """
    result = User(fbid=object_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_studies_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Studies for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_studies result
    """
    result = User(fbid=object_id).get_ad_studies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_albums_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Albums for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_albums result
    """
    result = User(fbid=object_id).get_albums(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_app_request_former_recipients_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get App Request Former Recipients for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_app_request_former_recipients result
    """
    result = User(fbid=object_id).get_app_request_former_recipients(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_app_requests_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get App Requests for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_app_requests result
    """
    result = User(fbid=object_id).get_app_requests(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_ad_accounts_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Assigned Ad Accounts for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_assigned_ad_accounts result
    """
    result = User(fbid=object_id).get_assigned_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_applications_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Assigned Applications for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_assigned_applications result
    """
    result = User(fbid=object_id).get_assigned_applications(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_business_asset_groups_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Assigned Business Asset Groups for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_assigned_business_asset_groups result
    """
    result = User(fbid=object_id).get_assigned_business_asset_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_pages_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Assigned Pages for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_assigned_pages result
    """
    result = User(fbid=object_id).get_assigned_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_product_catalogs_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Assigned Product Catalogs for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_assigned_product_catalogs result
    """
    result = User(fbid=object_id).get_assigned_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_avatars_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Avatars for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_avatars result
    """
    result = User(fbid=object_id).get_avatars(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_business_users_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Business Users for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_business_users result
    """
    result = User(fbid=object_id).get_business_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_businesses_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Businesses for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_businesses result
    """
    result = User(fbid=object_id).get_businesses(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_conversations_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Conversations for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_conversations result
    """
    result = User(fbid=object_id).get_conversations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_custom_labels_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Custom Labels for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_custom_labels result
    """
    result = User(fbid=object_id).get_custom_labels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_events_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Events for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_events result
    """
    result = User(fbid=object_id).get_events(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_feed_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Feed for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_feed result
    """
    result = User(fbid=object_id).get_feed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_friends_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Friends for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_friends result
    """
    result = User(fbid=object_id).get_friends(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_fundraisers_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Fundraisers for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_fundraisers result
    """
    result = User(fbid=object_id).get_fundraisers(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_groups_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Groups for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_groups result
    """
    result = User(fbid=object_id).get_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ids_for_apps_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ids For Apps for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ids_for_apps result
    """
    result = User(fbid=object_id).get_ids_for_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ids_for_business_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ids For Business for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ids_for_business result
    """
    result = User(fbid=object_id).get_ids_for_business(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ids_for_pages_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ids For Pages for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ids_for_pages result
    """
    result = User(fbid=object_id).get_ids_for_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_likes_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Likes for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_likes result
    """
    result = User(fbid=object_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_live_videos_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Live Videos for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_live_videos result
    """
    result = User(fbid=object_id).get_live_videos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_music_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Music for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_music result
    """
    result = User(fbid=object_id).get_music(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_payment_transactions_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Payment Transactions for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_payment_transactions result
    """
    result = User(fbid=object_id).get_payment_transactions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_permissions_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Permissions for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_permissions result
    """
    result = User(fbid=object_id).get_permissions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_personal_ad_accounts_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Personal Ad Accounts for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_personal_ad_accounts result
    """
    result = User(fbid=object_id).get_personal_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_photos_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Photos for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_photos result
    """
    result = User(fbid=object_id).get_photos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_picture_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Picture for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_picture result
    """
    result = User(fbid=object_id).get_picture(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_posts_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Posts for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_posts result
    """
    result = User(fbid=object_id).get_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_rich_media_documents_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Rich Media Documents for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_rich_media_documents result
    """
    result = User(fbid=object_id).get_rich_media_documents(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_videos_for_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Videos for User.

    Args:
        object_id: The ID of the User
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_videos result
    """
    result = User(fbid=object_id).get_videos(
        fields=fields,
        params=params,
    )

    return result


# Export the server
user_server = mcp
