"""
Auto-generated MCP server for Facebook IGUser.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.iguser import IGUser
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-iguser")


# CRUD Operations


@mcp.tool()
async def create_iguser(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_iguser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=object_id).api_update(
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
    result = IGUser(fbid=object_id).get_welcome_message_flows(
        fields=fields,
        params=params,
    )

    return result


# Export the server
iguser_server = mcp
