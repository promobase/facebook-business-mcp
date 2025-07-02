"""
Auto-generated MCP server for Facebook Destination.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.destination import Destination
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-destination")


# CRUD Operations


@mcp.tool()
async def get_destination(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Destination.

    Args:
        object_id: The ID of the Destination
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Destination(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_channels_to_integrity_status_for_destination(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Channels To Integrity Status for Destination.

    Args:
        object_id: The ID of the Destination
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_channels_to_integrity_status result
    """
    result = Destination(fbid=object_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_override_details_for_destination(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Override Details for Destination.

    Args:
        object_id: The ID of the Destination
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_override_details result
    """
    result = Destination(fbid=object_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_videos_metadata_for_destination(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Videos Metadata for Destination.

    Args:
        object_id: The ID of the Destination
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_videos_metadata result
    """
    result = Destination(fbid=object_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
destination_server = mcp
