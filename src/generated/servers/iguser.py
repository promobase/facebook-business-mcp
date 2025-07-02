"""
Auto-generated MCP server for Facebook IGUser.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.iguser import IGUser
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-iguser")


# CRUD Operations


@mcp.tool()
async def get_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = IGUser(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_authorized_ad_account_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Authorized Ad Account for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_authorized_ad_account result
    """
    result = IGUser(fbid=object_id).create_authorized_ad_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_branded_content_ad_permission_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Branded Content Ad Permission for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_branded_content_ad_permission result
    """
    result = IGUser(fbid=object_id).create_branded_content_ad_permission(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_branded_content_tag_approval_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Branded Content Tag Approval for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_branded_content_tag_approval result
    """
    result = IGUser(fbid=object_id).create_branded_content_tag_approval(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_dataset_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Dataset for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_dataset result
    """
    result = IGUser(fbid=object_id).create_dataset(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_media_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Media for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_media result
    """
    result = IGUser(fbid=object_id).create_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_media_publish_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Media Publish for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_media_publish result
    """
    result = IGUser(fbid=object_id).create_media_publish(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_mention_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Mention for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_mention result
    """
    result = IGUser(fbid=object_id).create_mention(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_product_appeal_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Product Appeal for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_product_appeal result
    """
    result = IGUser(fbid=object_id).create_product_appeal(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_upcoming_event_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Upcoming Event for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_upcoming_event result
    """
    result = IGUser(fbid=object_id).create_upcoming_event(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_branded_content_tag_approval_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Branded Content Tag Approval for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_branded_content_tag_approval result
    """
    result = IGUser(fbid=object_id).delete_branded_content_tag_approval(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_agencies_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Agencies for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_agencies result
    """
    result = IGUser(fbid=object_id).get_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_authorized_ad_accounts_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Authorized Ad Accounts for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_authorized_ad_accounts result
    """
    result = IGUser(fbid=object_id).get_authorized_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_available_catalogs_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Available Catalogs for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_available_catalogs result
    """
    result = IGUser(fbid=object_id).get_available_catalogs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_branded_content_ad_permissions_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Branded Content Ad Permissions for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_branded_content_ad_permissions result
    """
    result = IGUser(fbid=object_id).get_branded_content_ad_permissions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_branded_content_advertisable_medias_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Branded Content Advertisable Medias for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_branded_content_advertisable_medias result
    """
    result = IGUser(fbid=object_id).get_branded_content_advertisable_medias(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_branded_content_tag_approval_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Branded Content Tag Approval for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_branded_content_tag_approval result
    """
    result = IGUser(fbid=object_id).get_branded_content_tag_approval(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_catalog_product_search_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Catalog Product Search for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_catalog_product_search result
    """
    result = IGUser(fbid=object_id).get_catalog_product_search(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_connected_threads_user_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Connected Threads User for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_connected_threads_user result
    """
    result = IGUser(fbid=object_id).get_connected_threads_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_content_publishing_limit_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Content Publishing Limit for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_content_publishing_limit result
    """
    result = IGUser(fbid=object_id).get_content_publishing_limit(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_dataset_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Dataset for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_dataset result
    """
    result = IGUser(fbid=object_id).get_dataset(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Insights for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights result
    """
    result = IGUser(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_instagram_backed_threads_user_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Instagram Backed Threads User for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_instagram_backed_threads_user result
    """
    result = IGUser(fbid=object_id).get_instagram_backed_threads_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_live_media_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Live Media for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_live_media result
    """
    result = IGUser(fbid=object_id).get_live_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_media_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Media for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_media result
    """
    result = IGUser(fbid=object_id).get_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_notification_message_tokens_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Notification Message Tokens for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_notification_message_tokens result
    """
    result = IGUser(fbid=object_id).get_notification_message_tokens(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_product_appeal_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Product Appeal for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_product_appeal result
    """
    result = IGUser(fbid=object_id).get_product_appeal(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_recently_searched_hashtags_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Recently Searched Hashtags for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_recently_searched_hashtags result
    """
    result = IGUser(fbid=object_id).get_recently_searched_hashtags(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_stories_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Stories for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_stories result
    """
    result = IGUser(fbid=object_id).get_stories(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_tags_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Tags for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_tags result
    """
    result = IGUser(fbid=object_id).get_tags(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_upcoming_events_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Upcoming Events for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_upcoming_events result
    """
    result = IGUser(fbid=object_id).get_upcoming_events(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_welcome_message_flows_for_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Welcome Message Flows for IGUser.

    Args:
        object_id: The ID of the IGUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_welcome_message_flows result
    """
    result = IGUser(fbid=object_id).get_welcome_message_flows(
        fields=fields,
        params=params,
    )

    return result


# Export the server
iguser_server = mcp
