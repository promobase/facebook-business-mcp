"""
Auto-generated MCP server for Facebook Hotel.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.hotel import Hotel
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-hotel")


# CRUD Operations


@mcp.tool()
async def create_hotel(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a Hotel.

    Args:
        object_id: The ID of the Hotel
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = Hotel(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_hotel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a Hotel.

    Args:
        object_id: The ID of the Hotel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = Hotel(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_hotel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Hotel.

    Args:
        object_id: The ID of the Hotel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Hotel(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_hotel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a Hotel.

    Args:
        object_id: The ID of the Hotel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = Hotel(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_channels_to_integrity_status_for_hotel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Channels To Integrity Status for Hotel.

    Args:
        object_id: The ID of the Hotel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_channels_to_integrity_status result
    """
    result = Hotel(fbid=object_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_hotel_rooms_for_hotel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Hotel Rooms for Hotel.

    Args:
        object_id: The ID of the Hotel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_hotel_rooms result
    """
    result = Hotel(fbid=object_id).get_hotel_rooms(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_override_details_for_hotel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Override Details for Hotel.

    Args:
        object_id: The ID of the Hotel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_override_details result
    """
    result = Hotel(fbid=object_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_videos_metadata_for_hotel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Videos Metadata for Hotel.

    Args:
        object_id: The ID of the Hotel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_videos_metadata result
    """
    result = Hotel(fbid=object_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
hotel_server = mcp
