"""
Auto-generated MCP server for Facebook User.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.user import User
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-user")


# CRUD Operations


@mcp.tool()
async def create_user(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = User(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_user(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
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
    result = User(fbid=object_id).get_videos(
        fields=fields,
        params=params,
    )

    return result


# Export the server
user_server = mcp
