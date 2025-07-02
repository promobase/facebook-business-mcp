"""
Auto-generated MCP server for Facebook IGUserForIGOnlyAPI.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.iguserforigonlyapi import IGUserForIGOnlyAPI
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-iguserforigonlyapi")


# CRUD Operations


@mcp.tool()
async def get_iguserforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = IGUserForIGOnlyAPI(fbid=object_id).api_get(
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
    """
    Create Media for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_media result
    """
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
    """
    Create Media Publish for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_media_publish result
    """
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
    """
    Create Mention for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_mention result
    """
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
    """
    Create Message for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_message result
    """
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
    """
    Create Message Attachment for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_message_attachment result
    """
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
    """
    Create Messenger Profile for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_messenger_profile result
    """
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
    """
    Create Subscribed App for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_subscribed_app result
    """
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
    """
    Create Welcome Message Flow for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_welcome_message_flow result
    """
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
    """
    Delete Messenger Profile for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_messenger_profile result
    """
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
    """
    Delete Subscribed Apps for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_subscribed_apps result
    """
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
    """
    Delete Welcome Message Flows for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_welcome_message_flows result
    """
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
    """
    Get Business Messaging Feature Status for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_business_messaging_feature_status result
    """
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
    """
    Get Content Publishing Limit for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_content_publishing_limit result
    """
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
    """
    Get Conversations for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_conversations result
    """
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
    """
    Get Insights for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights result
    """
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
    """
    Get Live Media for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_live_media result
    """
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
    """
    Get Media for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_media result
    """
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
    """
    Get Messenger Profile for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_messenger_profile result
    """
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
    """
    Get Stories for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_stories result
    """
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
    """
    Get Subscribed Apps for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_subscribed_apps result
    """
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
    """
    Get Tags for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_tags result
    """
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
    """
    Get Welcome Message Flows for IGUserForIGOnlyAPI.

    Args:
        object_id: The ID of the IGUserForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_welcome_message_flows result
    """
    result = IGUserForIGOnlyAPI(fbid=object_id).get_welcome_message_flows(
        fields=fields,
        params=params,
    )

    return result


# Export the server
iguserforigonlyapi_server = mcp
