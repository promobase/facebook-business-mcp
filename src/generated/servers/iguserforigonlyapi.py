"""
Auto-generated MCP server for Facebook IGUserForIGOnlyAPI.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.iguserforigonlyapi import IGUserForIGOnlyAPI
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-iguserforigonlyapi")


# CRUD Operations


@mcp.tool()
async def create_iguserforigonlyapi(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_media_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).create_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_media_publish_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).create_media_publish(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_mention_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).create_mention(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_message_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).create_message(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_message_attachment_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).create_message_attachment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_messenger_profile_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).create_messenger_profile(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_subscribed_app_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).create_subscribed_app(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_welcome_message_flow_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).create_welcome_message_flow(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_messenger_profile_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).delete_messenger_profile(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_subscribed_apps_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).delete_subscribed_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_welcome_message_flows_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).delete_welcome_message_flows(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_business_messaging_feature_status_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).get_business_messaging_feature_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_content_publishing_limit_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).get_content_publishing_limit(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_conversations_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).get_conversations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_live_media_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).get_live_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_media_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).get_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_messenger_profile_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).get_messenger_profile(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_stories_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).get_stories(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_subscribed_apps_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).get_subscribed_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_tags_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).get_tags(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_welcome_message_flows_for_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=object_id).get_welcome_message_flows(
        fields=fields,
        params=params,
    )

    return result


# Export the server
iguserforigonlyapi_server = mcp
