"""
Auto-generated MCP server for Facebook InstagramUser.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.instagramuser import InstagramUser
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-instagramuser")


# CRUD Operations


@mcp.tool()
async def get_instagramuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a InstagramUser.

    Args:
        object_id: The ID of the InstagramUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = InstagramUser(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_agencies_for_instagramuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Agencies for InstagramUser.

    Args:
        object_id: The ID of the InstagramUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_agencies result
    """
    result = InstagramUser(fbid=object_id).get_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ar_effects_for_instagramuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ar Effects for InstagramUser.

    Args:
        object_id: The ID of the InstagramUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ar_effects result
    """
    result = InstagramUser(fbid=object_id).get_ar_effects(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_authorized_ad_accounts_for_instagramuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Authorized Ad Accounts for InstagramUser.

    Args:
        object_id: The ID of the InstagramUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_authorized_ad_accounts result
    """
    result = InstagramUser(fbid=object_id).get_authorized_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_upcoming_events_for_instagramuser(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Upcoming Events for InstagramUser.

    Args:
        object_id: The ID of the InstagramUser
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_upcoming_events result
    """
    result = InstagramUser(fbid=object_id).get_upcoming_events(
        fields=fields,
        params=params,
    )

    return result


# Export the server
instagramuser_server = mcp
