"""
Auto-generated MCP server for Facebook MediaTitle.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.mediatitle import MediaTitle
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-mediatitle")


# CRUD Operations


@mcp.tool()
async def delete_mediatitle(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a MediaTitle.

    Args:
        object_id: The ID of the MediaTitle
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = MediaTitle(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_mediatitle(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a MediaTitle.

    Args:
        object_id: The ID of the MediaTitle
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = MediaTitle(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_mediatitle(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a MediaTitle.

    Args:
        object_id: The ID of the MediaTitle
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = MediaTitle(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_channels_to_integrity_status_for_mediatitle(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Channels To Integrity Status for MediaTitle.

    Args:
        object_id: The ID of the MediaTitle
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_channels_to_integrity_status result
    """
    result = MediaTitle(fbid=object_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_override_details_for_mediatitle(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Override Details for MediaTitle.

    Args:
        object_id: The ID of the MediaTitle
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_override_details result
    """
    result = MediaTitle(fbid=object_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_videos_metadata_for_mediatitle(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Videos Metadata for MediaTitle.

    Args:
        object_id: The ID of the MediaTitle
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_videos_metadata result
    """
    result = MediaTitle(fbid=object_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
mediatitle_server = mcp
