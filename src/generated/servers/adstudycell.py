"""
Auto-generated MCP server for Facebook AdStudyCell.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adstudycell import AdStudyCell
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adstudycell")


# CRUD Operations


@mcp.tool()
async def get_adstudycell(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdStudyCell.

    Args:
        object_id: The ID of the AdStudyCell
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdStudyCell(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adstudycell(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a AdStudyCell.

    Args:
        object_id: The ID of the AdStudyCell
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = AdStudyCell(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_ad_accounts_for_adstudycell(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Accounts for AdStudyCell.

    Args:
        object_id: The ID of the AdStudyCell
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_accounts result
    """
    result = AdStudyCell(fbid=object_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_sets_for_adstudycell(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Sets for AdStudyCell.

    Args:
        object_id: The ID of the AdStudyCell
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_sets result
    """
    result = AdStudyCell(fbid=object_id).get_ad_sets(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_campaigns_for_adstudycell(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Campaigns for AdStudyCell.

    Args:
        object_id: The ID of the AdStudyCell
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_campaigns result
    """
    result = AdStudyCell(fbid=object_id).get_campaigns(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adstudycell_server = mcp
