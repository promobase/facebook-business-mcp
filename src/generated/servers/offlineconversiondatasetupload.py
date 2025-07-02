"""
Auto-generated MCP server for Facebook OfflineConversionDataSetUpload.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.offlineconversiondatasetupload import (
    OfflineConversionDataSetUpload,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-offlineconversiondatasetupload")


# CRUD Operations


@mcp.tool()
async def create_offlineconversiondatasetupload(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineConversionDataSetUpload(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_offlineconversiondatasetupload(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineConversionDataSetUpload(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_offlineconversiondatasetupload(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineConversionDataSetUpload(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_offlineconversiondatasetupload(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineConversionDataSetUpload(fbid=object_id).api_update(
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
    result = OfflineConversionDataSetUpload(fbid=object_id).get_pull_sessions(
        fields=fields,
        params=params,
    )

    return result


# Export the server
offlineconversiondatasetupload_server = mcp
