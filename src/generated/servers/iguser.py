"""IGUser MCP Server."""

from typing import Any

from facebook_business.adobjects.iguser import IGUser
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGUser"
instructions = """
IGUser MCP Server for Facebook Business API.

Provides typed access to all IGUser operations.
"""

iguser_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@iguser_server.tool
@wrapped_fn_tool
def get_iguser(
    iguser_id: str,
    fields: list[str] = [],
) -> str:
    obj = IGUser(iguser_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (31) ----
@iguser_server.tool
@wrapped_fn_tool
def get_agencies(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_agencies(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_authorized_adaccounts(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_authorized_adaccounts(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_authorized_adaccount(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).create_authorized_adaccount(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_available_catalogs(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_available_catalogs(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_branded_content_ad_permissions(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_branded_content_ad_permissions(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_branded_content_ad_permission(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).create_branded_content_ad_permission(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_branded_content_advertisable_medias(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_branded_content_advertisable_medias(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def delete_branded_content_tag_approval(
    iguser_id: str,
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).delete_branded_content_tag_approval(params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_branded_content_tag_approval(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_branded_content_tag_approval(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_branded_content_tag_approval(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).create_branded_content_tag_approval(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_catalog_product_search(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_catalog_product_search(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_connected_threads_user(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_connected_threads_user(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_content_publishing_limit(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_content_publishing_limit(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_dataset(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_dataset(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_dataset(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).create_dataset(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_insights(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_insights(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_instagram_backed_threads_user(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_instagram_backed_threads_user(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_live_media(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_live_media(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_media(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_media(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_media(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).create_media(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_media_publish(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).create_media_publish(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_mention(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).create_mention(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_notification_message_tokens(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_notification_message_tokens(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_product_appeal(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_product_appeal(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_product_appeal(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).create_product_appeal(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_recently_searched_hashtags(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_recently_searched_hashtags(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_stories(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_stories(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_tags(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_tags(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_upcoming_events(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_upcoming_events(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_upcoming_event(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).create_upcoming_event(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def get_welcome_message_flows(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_welcome_message_flows(fields=fields, params=params)
