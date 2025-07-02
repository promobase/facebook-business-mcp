"""
Auto-generated MCP server for Facebook HomeListing.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.homelisting import HomeListing
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-homelisting")


# CRUD Operations


@mcp.tool()
async def create_homelisting(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a HomeListing.

    Args:
        object_id: The ID of the HomeListing
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = HomeListing(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_homelisting(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a HomeListing.

    Args:
        object_id: The ID of the HomeListing
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = HomeListing(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_homelisting(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a HomeListing.

    Args:
        object_id: The ID of the HomeListing
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = HomeListing(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_homelisting(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a HomeListing.

    Args:
        object_id: The ID of the HomeListing
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = HomeListing(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_channels_to_integrity_status_for_homelisting(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Channels To Integrity Status for HomeListing.

    Args:
        object_id: The ID of the HomeListing
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_channels_to_integrity_status result
    """
    result = HomeListing(fbid=object_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_override_details_for_homelisting(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Override Details for HomeListing.

    Args:
        object_id: The ID of the HomeListing
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_override_details result
    """
    result = HomeListing(fbid=object_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_videos_metadata_for_homelisting(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Videos Metadata for HomeListing.

    Args:
        object_id: The ID of the HomeListing
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_videos_metadata result
    """
    result = HomeListing(fbid=object_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
homelisting_server = mcp
