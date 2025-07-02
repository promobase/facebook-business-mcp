"""
Auto-generated MCP server for Facebook ContentBlockList.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.contentblocklist import ContentBlockList
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-contentblocklist")


# CRUD Operations


@mcp.tool()
async def get_contentblocklist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ContentBlockList.

    Args:
        object_id: The ID of the ContentBlockList
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ContentBlockList(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_applied_ad_accounts_for_contentblocklist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Applied Ad Accounts for ContentBlockList.

    Args:
        object_id: The ID of the ContentBlockList
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_applied_ad_accounts result
    """
    result = ContentBlockList(fbid=object_id).get_applied_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_facebook_content_for_contentblocklist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Facebook Content for ContentBlockList.

    Args:
        object_id: The ID of the ContentBlockList
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_facebook_content result
    """
    result = ContentBlockList(fbid=object_id).get_facebook_content(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_instagram_content_for_contentblocklist(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Instagram Content for ContentBlockList.

    Args:
        object_id: The ID of the ContentBlockList
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_instagram_content result
    """
    result = ContentBlockList(fbid=object_id).get_instagram_content(
        fields=fields,
        params=params,
    )

    return result


# Export the server
contentblocklist_server = mcp
