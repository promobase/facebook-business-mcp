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


# ---- Edge Methods (20) ----
@iguser_server.tool
@wrapped_fn_tool
def get_authorized_ad_accounts(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_authorized_ad_accounts(fields=fields, params=params)


@iguser_server.tool
@wrapped_fn_tool
def create_authorized_ad_account(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).create_authorized_ad_account(fields=fields, params=params)


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
def get_content_publishing_limit(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUser(iguser_id).get_content_publishing_limit(fields=fields, params=params)


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
