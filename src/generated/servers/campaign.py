"""
Auto-generated MCP server for Facebook Campaign.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.campaign import Campaign
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-campaign")


# CRUD Operations


@mcp.tool()
async def create_campaign(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_campaign(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_campaign(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_campaign(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_ad_label_for_campaign(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=object_id).create_ad_label(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_budget_schedule_for_campaign(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=object_id).create_budget_schedule(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_copy_for_campaign(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=object_id).create_copy(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_rules_governed_for_campaign(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=object_id).get_ad_rules_governed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_sets_for_campaign(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=object_id).get_ad_sets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_studies_for_campaign(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=object_id).get_ad_studies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ads_for_campaign(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=object_id).get_ads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_copies_for_campaign(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=object_id).get_copies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_for_campaign(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_async_for_campaign(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=object_id).get_insights_async(
        fields=fields,
        params=params,
    )

    return result


# Export the server
campaign_server = mcp
