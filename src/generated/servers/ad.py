"""
Auto-generated MCP server for Facebook Ad.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.ad import Ad
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-ad")


# CRUD Operations


@mcp.tool()
async def create_ad(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a Ad.

    Args:
        object_id: The ID of the Ad
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = Ad(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a Ad.

    Args:
        object_id: The ID of the Ad
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = Ad(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Ad.

    Args:
        object_id: The ID of the Ad
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Ad(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a Ad.

    Args:
        object_id: The ID of the Ad
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = Ad(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_ad_label_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ad Label for Ad.

    Args:
        object_id: The ID of the Ad
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_label result
    """
    result = Ad(fbid=object_id).create_ad_label(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_copy_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Copy for Ad.

    Args:
        object_id: The ID of the Ad
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_copy result
    """
    result = Ad(fbid=object_id).create_copy(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_creatives_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Creatives for Ad.

    Args:
        object_id: The ID of the Ad
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_creatives result
    """
    result = Ad(fbid=object_id).get_ad_creatives(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_rules_governed_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Rules Governed for Ad.

    Args:
        object_id: The ID of the Ad
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_rules_governed result
    """
    result = Ad(fbid=object_id).get_ad_rules_governed(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_copies_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Copies for Ad.

    Args:
        object_id: The ID of the Ad
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_copies result
    """
    result = Ad(fbid=object_id).get_copies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Insights for Ad.

    Args:
        object_id: The ID of the Ad
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights result
    """
    result = Ad(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_async_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Insights Async for Ad.

    Args:
        object_id: The ID of the Ad
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights_async result
    """
    result = Ad(fbid=object_id).get_insights_async(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_leads_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Leads for Ad.

    Args:
        object_id: The ID of the Ad
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_leads result
    """
    result = Ad(fbid=object_id).get_leads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_previews_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Previews for Ad.

    Args:
        object_id: The ID of the Ad
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_previews result
    """
    result = Ad(fbid=object_id).get_previews(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_targeting_sentence_lines_for_ad(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Targeting Sentence Lines for Ad.

    Args:
        object_id: The ID of the Ad
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_targeting_sentence_lines result
    """
    result = Ad(fbid=object_id).get_targeting_sentence_lines(
        fields=fields,
        params=params,
    )

    return result


# Export the server
ad_server = mcp
