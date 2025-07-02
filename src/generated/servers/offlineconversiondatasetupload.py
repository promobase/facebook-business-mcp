"""
Auto-generated MCP server for Facebook OfflineConversionDataSetUpload.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.offlineconversiondatasetupload import (
    OfflineConversionDataSetUpload,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-offlineconversiondatasetupload")


# CRUD Operations


@mcp.tool()
async def get_offlineconversiondatasetupload(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a OfflineConversionDataSetUpload.

    Args:
        object_id: The ID of the OfflineConversionDataSetUpload
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = OfflineConversionDataSetUpload(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_progress_for_offlineconversiondatasetupload(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Progress for OfflineConversionDataSetUpload.

    Args:
        object_id: The ID of the OfflineConversionDataSetUpload
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_progress result
    """
    result = OfflineConversionDataSetUpload(fbid=object_id).get_progress(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pull_sessions_for_offlineconversiondatasetupload(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Pull Sessions for OfflineConversionDataSetUpload.

    Args:
        object_id: The ID of the OfflineConversionDataSetUpload
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_pull_sessions result
    """
    result = OfflineConversionDataSetUpload(fbid=object_id).get_pull_sessions(
        fields=fields,
        params=params,
    )

    return result


# Export the server
offlineconversiondatasetupload_server = mcp
