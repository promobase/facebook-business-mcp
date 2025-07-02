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
async def api_create_campaign(
    campaign_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=campaign_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_campaign(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=campaign_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_campaign(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=campaign_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_campaign(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=campaign_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_ad_label(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=campaign_id).create_ad_label(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_budget_schedule(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=campaign_id).create_budget_schedule(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_copy(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=campaign_id).create_copy(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_rules_governed(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=campaign_id).get_ad_rules_governed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_sets(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=campaign_id).get_ad_sets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_studies(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=campaign_id).get_ad_studies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ads(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=campaign_id).get_ads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_copies(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=campaign_id).get_copies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=campaign_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_async(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Campaign(fbid=campaign_id).get_insights_async(
        fields=fields,
        params=params,
    )

    return result


# Export the server
campaign_server = mcp
