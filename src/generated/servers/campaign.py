"""
Auto-generated MCP server for Facebook Campaign.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi
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
    """
    Create a Campaign.

    Args:
        object_id: The ID of the Campaign
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
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
    """
    Delete a Campaign.

    Args:
        object_id: The ID of the Campaign
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
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
    """
    Get a Campaign.

    Args:
        object_id: The ID of the Campaign
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
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
    """
    Update a Campaign.

    Args:
        object_id: The ID of the Campaign
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
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
    """
    Create Ad Label for Campaign.

    Args:
        object_id: The ID of the Campaign
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_label result
    """
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
    """
    Create Budget Schedule for Campaign.

    Args:
        object_id: The ID of the Campaign
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_budget_schedule result
    """
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
    """
    Create Copy for Campaign.

    Args:
        object_id: The ID of the Campaign
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_copy result
    """
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
    """
    Get Ad Rules Governed for Campaign.

    Args:
        object_id: The ID of the Campaign
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_rules_governed result
    """
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
    """
    Get Ad Sets for Campaign.

    Args:
        object_id: The ID of the Campaign
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_sets result
    """
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
    """
    Get Ad Studies for Campaign.

    Args:
        object_id: The ID of the Campaign
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_studies result
    """
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
    """
    Get Ads for Campaign.

    Args:
        object_id: The ID of the Campaign
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ads result
    """
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
    """
    Get Copies for Campaign.

    Args:
        object_id: The ID of the Campaign
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_copies result
    """
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
    """
    Get Insights for Campaign.

    Args:
        object_id: The ID of the Campaign
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights result
    """
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
    """
    Get Insights Async for Campaign.

    Args:
        object_id: The ID of the Campaign
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights_async result
    """
    result = Campaign(fbid=object_id).get_insights_async(
        fields=fields,
        params=params,
    )

    return result


# Export the server
campaign_server = mcp
