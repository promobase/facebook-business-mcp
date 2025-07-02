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
async def api_create_iguserforigonlyapi(
    iguserforigonlyapi_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_iguserforigonlyapi(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_iguserforigonlyapi(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_iguserforigonlyapi(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_media(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).create_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_media_publish(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).create_media_publish(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_mention(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).create_mention(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_message(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).create_message(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_message_attachment(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).create_message_attachment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_messenger_profile(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).create_messenger_profile(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_subscribed_app(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).create_subscribed_app(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_welcome_message_flow(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).create_welcome_message_flow(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_messenger_profile(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).delete_messenger_profile(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_subscribed_apps(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).delete_subscribed_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_welcome_message_flows(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).delete_welcome_message_flows(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_business_messaging_feature_status(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).get_business_messaging_feature_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_content_publishing_limit(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).get_content_publishing_limit(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_conversations(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).get_conversations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_live_media(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).get_live_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_media(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).get_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_messenger_profile(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).get_messenger_profile(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_stories(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).get_stories(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_subscribed_apps(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).get_subscribed_apps(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_tags(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).get_tags(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_welcome_message_flows(
    iguserforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUserForIGOnlyAPI(fbid=iguserforigonlyapi_id).get_welcome_message_flows(
        fields=fields,
        params=params,
    )

    return result


# Export the server
iguserforigonlyapi_server = mcp
