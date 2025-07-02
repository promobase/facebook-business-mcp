"""
Auto-generated MCP server for Facebook Vehicle.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.vehicle import Vehicle
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-vehicle")


# CRUD Operations


@mcp.tool()
async def create_vehicle(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a Vehicle.

    Args:
        object_id: The ID of the Vehicle
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = Vehicle(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_vehicle(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Vehicle.

    Args:
        object_id: The ID of the Vehicle
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Vehicle(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_vehicle(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a Vehicle.

    Args:
        object_id: The ID of the Vehicle
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = Vehicle(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_channels_to_integrity_status_for_vehicle(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Channels To Integrity Status for Vehicle.

    Args:
        object_id: The ID of the Vehicle
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_channels_to_integrity_status result
    """
    result = Vehicle(fbid=object_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_override_details_for_vehicle(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Override Details for Vehicle.

    Args:
        object_id: The ID of the Vehicle
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_override_details result
    """
    result = Vehicle(fbid=object_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_videos_metadata_for_vehicle(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Videos Metadata for Vehicle.

    Args:
        object_id: The ID of the Vehicle
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_videos_metadata result
    """
    result = Vehicle(fbid=object_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
vehicle_server = mcp
