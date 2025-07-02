"""
Auto-generated MCP server for Facebook Flight.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.flight import Flight
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-flight")


# CRUD Operations


@mcp.tool()
async def get_flight(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Flight.

    Args:
        object_id: The ID of the Flight
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Flight(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_flight(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a Flight.

    Args:
        object_id: The ID of the Flight
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = Flight(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_channels_to_integrity_status_for_flight(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Channels To Integrity Status for Flight.

    Args:
        object_id: The ID of the Flight
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_channels_to_integrity_status result
    """
    result = Flight(fbid=object_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_override_details_for_flight(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Override Details for Flight.

    Args:
        object_id: The ID of the Flight
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_override_details result
    """
    result = Flight(fbid=object_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_videos_metadata_for_flight(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Videos Metadata for Flight.

    Args:
        object_id: The ID of the Flight
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_videos_metadata result
    """
    result = Flight(fbid=object_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
flight_server = mcp
