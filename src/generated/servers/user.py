"""
Auto-generated MCP server for Facebook User.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.user import User
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-user")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    user_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_access_token(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).create_access_token(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_account(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).create_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_ad_study(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).create_ad_study(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_application(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).create_application(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_business(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).create_business(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_feed(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).create_feed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_fundraiser(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).create_fundraiser(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_live_video(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).create_live_video(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_messenger_desktop_performance_trace(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).create_messenger_desktop_performance_trace(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_messenger_kids_accounts_unread_badge(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).create_messenger_kids_accounts_unread_badge(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_notification(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).create_notification(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_photo(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).create_photo(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_staging_resource(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).create_staging_resource(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_video(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).create_video(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_access_tokens(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).delete_access_tokens(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_businesses(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).delete_businesses(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_permissions(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).delete_permissions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_accounts(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ad_accounts(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ad_studies(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_ad_studies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_albums(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_albums(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_app_request_former_recipients(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_app_request_former_recipients(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_app_requests(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_app_requests(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_assigned_ad_accounts(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_assigned_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_assigned_applications(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_assigned_applications(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_assigned_business_asset_groups(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_assigned_business_asset_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_assigned_pages(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_assigned_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_assigned_product_catalogs(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_assigned_product_catalogs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_avatars(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_avatars(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_business_users(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_business_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_businesses(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_businesses(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_conversations(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_conversations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_custom_labels(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_custom_labels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_events(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_events(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_feed(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_feed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_friends(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_friends(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_fundraisers(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_fundraisers(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_groups(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_groups(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ids_for_apps(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_ids_for_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ids_for_business(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_ids_for_business(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_ids_for_pages(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_ids_for_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_likes(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_live_videos(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_live_videos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_music(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_music(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_payment_transactions(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_payment_transactions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_permissions(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_permissions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_personal_ad_accounts(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_personal_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_photos(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_photos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_picture(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_picture(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_posts(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_rich_media_documents(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_rich_media_documents(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_videos(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = User(fbid=user_id).get_videos(
        fields=fields,
        params=params,
    )

    return result


# Export the server
user_server = mcp
