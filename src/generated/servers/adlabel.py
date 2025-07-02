"""
Auto-generated MCP server for Facebook AdLabel.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adlabel import AdLabel
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adlabel")


# CRUD Operations


@mcp.tool()
async def create_adlabel(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a AdLabel.

    Args:
        object_id: The ID of the AdLabel
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = AdLabel(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_adlabel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a AdLabel.

    Args:
        object_id: The ID of the AdLabel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = AdLabel(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adlabel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdLabel.

    Args:
        object_id: The ID of the AdLabel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdLabel(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adlabel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a AdLabel.

    Args:
        object_id: The ID of the AdLabel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = AdLabel(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_ad_creatives_for_adlabel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Creatives for AdLabel.

    Args:
        object_id: The ID of the AdLabel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_creatives result
    """
    result = AdLabel(fbid=object_id).get_ad_creatives(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_sets_for_adlabel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Sets for AdLabel.

    Args:
        object_id: The ID of the AdLabel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_sets result
    """
    result = AdLabel(fbid=object_id).get_ad_sets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ads_for_adlabel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ads for AdLabel.

    Args:
        object_id: The ID of the AdLabel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ads result
    """
    result = AdLabel(fbid=object_id).get_ads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_campaigns_for_adlabel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Campaigns for AdLabel.

    Args:
        object_id: The ID of the AdLabel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_campaigns result
    """
    result = AdLabel(fbid=object_id).get_campaigns(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adlabel_server = mcp
