"""User MCP Server."""

from typing import Any

from facebook_business.adobjects.user import User
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = User(user_id)
    return obj.api_get(fields=fields)


@user_server.tool
@wrapped_fn_tool
def update_user(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return User(user_id).api_update(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def delete_user(
    user_id: str,
) -> str:
    return User(user_id).api_delete()


# ---- Edge Methods (35) ----
@user_server.tool
@wrapped_fn_tool
def create_access_token(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).create_access_token(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_accounts(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_accounts(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_account(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).create_account(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_ad_study(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).create_ad_study(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_application(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).create_application(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_assigned_business_asset_groups(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_assigned_business_asset_groups(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_assigned_pages(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_assigned_pages(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def delete_businesses(
    user_id: str,
    params: dict[str, Any] = {},
):
    return User(user_id).delete_businesses(params=params)


@user_server.tool
@wrapped_fn_tool
def create_business(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).create_business(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_conversations(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_conversations(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_events(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_events(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_feed(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_feed(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_feed(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).create_feed(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_friends(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_friends(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_fundraiser(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).create_fundraiser(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_groups(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_groups(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_ids_for_apps(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_ids_for_apps(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_ids_for_business(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_ids_for_business(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_ids_for_pages(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_ids_for_pages(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_likes(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_likes(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_live_videos(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_live_videos(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_live_video(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).create_live_video(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_messenger_kids_accounts_unread_badge(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).create_messenger_kids_accounts_unread_badge(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_music(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_music(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_notification(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).create_notification(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def delete_permissions(
    user_id: str,
    params: dict[str, Any] = {},
):
    return User(user_id).delete_permissions(params=params)


@user_server.tool
@wrapped_fn_tool
def get_permissions(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_permissions(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_photos(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_photos(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_photo(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).create_photo(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_picture(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_picture(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_posts(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_posts(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_rich_media_documents(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_rich_media_documents(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_staging_resource(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).create_staging_resource(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def get_videos(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).get_videos(fields=fields, params=params)


@user_server.tool
@wrapped_fn_tool
def create_video(
    user_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return User(user_id).create_video(fields=fields, params=params)
