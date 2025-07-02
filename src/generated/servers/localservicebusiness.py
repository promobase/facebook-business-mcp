"""
Auto-generated MCP server for Facebook LocalServiceBusiness.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.localservicebusiness import LocalServiceBusiness
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-localservicebusiness")


# CRUD Operations


@mcp.tool()
async def get_localservicebusiness(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a LocalServiceBusiness.

    Args:
        object_id: The ID of the LocalServiceBusiness
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = LocalServiceBusiness(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_channels_to_integrity_status_for_localservicebusiness(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Channels To Integrity Status for LocalServiceBusiness.

    Args:
        object_id: The ID of the LocalServiceBusiness
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_channels_to_integrity_status result
    """
    result = LocalServiceBusiness(fbid=object_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_override_details_for_localservicebusiness(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Override Details for LocalServiceBusiness.

    Args:
        object_id: The ID of the LocalServiceBusiness
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_override_details result
    """
    result = LocalServiceBusiness(fbid=object_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


# Export the server
localservicebusiness_server = mcp
