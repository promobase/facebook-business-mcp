"""
Auto-generated MCP server for Facebook AdCreative.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adcreative")


# CRUD Operations


@mcp.tool()
async def create_adcreative(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a AdCreative.

    Args:
        object_id: The ID of the AdCreative
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = AdCreative(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_adcreative(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a AdCreative.

    Args:
        object_id: The ID of the AdCreative
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = AdCreative(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adcreative(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdCreative.

    Args:
        object_id: The ID of the AdCreative
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdCreative(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adcreative(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a AdCreative.

    Args:
        object_id: The ID of the AdCreative
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = AdCreative(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_ad_label_for_adcreative(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ad Label for AdCreative.

    Args:
        object_id: The ID of the AdCreative
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ad_label result
    """
    result = AdCreative(fbid=object_id).create_ad_label(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_creative_insights_for_adcreative(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Creative Insights for AdCreative.

    Args:
        object_id: The ID of the AdCreative
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_creative_insights result
    """
    result = AdCreative(fbid=object_id).get_creative_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_previews_for_adcreative(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Previews for AdCreative.

    Args:
        object_id: The ID of the AdCreative
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_previews result
    """
    result = AdCreative(fbid=object_id).get_previews(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adcreative_server = mcp
