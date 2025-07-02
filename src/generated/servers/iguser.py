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
async def api_create_iguser(
    iguser_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_iguser(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_iguser(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_iguser(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_authorized_ad_account(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).create_authorized_ad_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_branded_content_ad_permission(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).create_branded_content_ad_permission(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_branded_content_tag_approval(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).create_branded_content_tag_approval(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_dataset(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).create_dataset(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_media(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).create_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_media_publish(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).create_media_publish(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_mention(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).create_mention(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_product_appeal(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).create_product_appeal(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_upcoming_event(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).create_upcoming_event(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_branded_content_tag_approval(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).delete_branded_content_tag_approval(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_agencies(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_authorized_ad_accounts(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_authorized_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_available_catalogs(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_available_catalogs(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_branded_content_ad_permissions(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_branded_content_ad_permissions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_branded_content_advertisable_medias(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_branded_content_advertisable_medias(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_branded_content_tag_approval(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_branded_content_tag_approval(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_catalog_product_search(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_catalog_product_search(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_connected_threads_user(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_connected_threads_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_content_publishing_limit(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_content_publishing_limit(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_dataset(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_dataset(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_instagram_backed_threads_user(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_instagram_backed_threads_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_live_media(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_live_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_media(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_media(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_notification_message_tokens(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_notification_message_tokens(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_product_appeal(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_product_appeal(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_recently_searched_hashtags(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_recently_searched_hashtags(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_stories(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_stories(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_tags(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_tags(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_upcoming_events(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_upcoming_events(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_welcome_message_flows(
    iguser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUser(fbid=iguser_id).get_welcome_message_flows(
        fields=fields,
        params=params,
    )

    return result


# Export the server
iguser_server = mcp
