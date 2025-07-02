"""
Auto-generated MCP server for Facebook VehicleOffer.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.vehicleoffer import VehicleOffer
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-vehicleoffer")


# CRUD Operations


@mcp.tool()
async def get_vehicleoffer(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a VehicleOffer.

    Args:
        object_id: The ID of the VehicleOffer
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = VehicleOffer(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_channels_to_integrity_status_for_vehicleoffer(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Channels To Integrity Status for VehicleOffer.

    Args:
        object_id: The ID of the VehicleOffer
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_channels_to_integrity_status result
    """
    result = VehicleOffer(fbid=object_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_override_details_for_vehicleoffer(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Override Details for VehicleOffer.

    Args:
        object_id: The ID of the VehicleOffer
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_override_details result
    """
    result = VehicleOffer(fbid=object_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_videos_metadata_for_vehicleoffer(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Videos Metadata for VehicleOffer.

    Args:
        object_id: The ID of the VehicleOffer
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_videos_metadata result
    """
    result = VehicleOffer(fbid=object_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
vehicleoffer_server = mcp
