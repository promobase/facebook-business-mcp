"""
Auto-generated MCP server for Facebook AdSet.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adset")


# CRUD Operations


@mcp.tool()
async def create_adset(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a AdSet.

    Args:
        object_id: The ID of the AdSet
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = AdSet(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = AdSet(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdSet(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = AdSet(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_ad_label_for_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ad Label for AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_label result
    """
    result = AdSet(fbid=object_id).create_ad_label(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_budget_schedule_for_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Budget Schedule for AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_budget_schedule result
    """
    result = AdSet(fbid=object_id).create_budget_schedule(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_copy_for_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Copy for AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_copy result
    """
    result = AdSet(fbid=object_id).create_copy(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_ad_labels_for_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Ad Labels for AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_ad_labels result
    """
    result = AdSet(fbid=object_id).delete_ad_labels(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_activities_for_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Activities for AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_activities result
    """
    result = AdSet(fbid=object_id).get_activities(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_creatives_for_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Creatives for AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_creatives result
    """
    result = AdSet(fbid=object_id).get_ad_creatives(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_rules_governed_for_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Rules Governed for AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_rules_governed result
    """
    result = AdSet(fbid=object_id).get_ad_rules_governed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_studies_for_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Studies for AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_studies result
    """
    result = AdSet(fbid=object_id).get_ad_studies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ads_for_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ads for AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ads result
    """
    result = AdSet(fbid=object_id).get_ads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_async_ad_requests_for_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Async Ad Requests for AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_async_ad_requests result
    """
    result = AdSet(fbid=object_id).get_async_ad_requests(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_copies_for_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Copies for AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_copies result
    """
    result = AdSet(fbid=object_id).get_copies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_delivery_estimate_for_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Delivery Estimate for AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_delivery_estimate result
    """
    result = AdSet(fbid=object_id).get_delivery_estimate(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_for_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Insights for AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights result
    """
    result = AdSet(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_async_for_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Insights Async for AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights_async result
    """
    result = AdSet(fbid=object_id).get_insights_async(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_message_delivery_estimate_for_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Message Delivery Estimate for AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_message_delivery_estimate result
    """
    result = AdSet(fbid=object_id).get_message_delivery_estimate(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_targeting_sentence_lines_for_adset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Targeting Sentence Lines for AdSet.

    Args:
        object_id: The ID of the AdSet
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_targeting_sentence_lines result
    """
    result = AdSet(fbid=object_id).get_targeting_sentence_lines(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adset_server = mcp
