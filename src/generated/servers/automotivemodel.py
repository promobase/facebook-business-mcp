"""
Auto-generated MCP server for Facebook AutomotiveModel.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.automotivemodel import AutomotiveModel
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-automotivemodel")


# CRUD Operations


@mcp.tool()
async def get_automotivemodel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AutomotiveModel.

    Args:
        object_id: The ID of the AutomotiveModel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AutomotiveModel(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_channels_to_integrity_status_for_automotivemodel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Channels To Integrity Status for AutomotiveModel.

    Args:
        object_id: The ID of the AutomotiveModel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_channels_to_integrity_status result
    """
    result = AutomotiveModel(fbid=object_id).get_channels_to_integrity_status(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_override_details_for_automotivemodel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Override Details for AutomotiveModel.

    Args:
        object_id: The ID of the AutomotiveModel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_override_details result
    """
    result = AutomotiveModel(fbid=object_id).get_override_details(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_videos_metadata_for_automotivemodel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Videos Metadata for AutomotiveModel.

    Args:
        object_id: The ID of the AutomotiveModel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_videos_metadata result
    """
    result = AutomotiveModel(fbid=object_id).get_videos_metadata(
        fields=fields,
        params=params,
    )

    return result


# Export the server
automotivemodel_server = mcp
