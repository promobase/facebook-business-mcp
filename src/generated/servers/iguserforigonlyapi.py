"""IGUserForIGOnlyAPI MCP Server."""

from typing import Any

from facebook_business.adobjects.iguserforigonlyapi import IGUserForIGOnlyAPI
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGUserForIGOnlyAPI"
instructions = """
IGUserForIGOnlyAPI MCP Server for Facebook Business API.

Provides typed access to all IGUserForIGOnlyAPI operations.
"""

iguserforigonlyapi_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_iguserforigonlyapi(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
) -> str:
    obj = IGUserForIGOnlyAPI(iguserforigonlyapi_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (22) ----
@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_business_messaging_feature_status(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).get_business_messaging_feature_status(
        fields=fields, params=params
    )


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_content_publishing_limit(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).get_content_publishing_limit(
        fields=fields, params=params
    )


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_conversations(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).get_conversations(fields=fields, params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_insights(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).get_insights(fields=fields, params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_live_media(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).get_live_media(fields=fields, params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_media(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).get_media(fields=fields, params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def create_media(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).create_media(fields=fields, params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def create_mediapublish(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).create_mediapublish(
        fields=fields, params=params
    )


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def create_mention(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).create_mention(fields=fields, params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def create_messageattachment(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).create_messageattachment(
        fields=fields, params=params
    )


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def create_message(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).create_message(fields=fields, params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def delete_messenger_profile(
    iguserforigonlyapi_id: str,
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).delete_messenger_profile(params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_messenger_profile(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).get_messenger_profile(
        fields=fields, params=params
    )


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def create_messenger_profile(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).create_messenger_profile(
        fields=fields, params=params
    )


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_stories(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).get_stories(fields=fields, params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def delete_subscribed_apps(
    iguserforigonlyapi_id: str,
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).delete_subscribed_apps(params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_subscribed_apps(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).get_subscribed_apps(
        fields=fields, params=params
    )


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def create_subscribed_app(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).create_subscribed_app(
        fields=fields, params=params
    )


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_tags(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).get_tags(fields=fields, params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def delete_welcome_message_flows(
    iguserforigonlyapi_id: str,
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).delete_welcome_message_flows(params=params)


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def get_welcome_message_flows(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).get_welcome_message_flows(
        fields=fields, params=params
    )


@iguserforigonlyapi_server.tool
@wrapped_fn_tool
def create_welcome_message_flow(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGUserForIGOnlyAPI(iguserforigonlyapi_id).create_welcome_message_flow(
        fields=fields, params=params
    )
