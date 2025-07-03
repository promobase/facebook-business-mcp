"""
Auto-generated MCP server for Facebook OfflineConversionDataSetUpload.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.offlineconversiondatasetupload import (
    OfflineConversionDataSetUpload,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-offlineconversiondatasetupload")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    offlineconversiondatasetupload_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSetUpload(fbid=offlineconversiondatasetupload_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    offlineconversiondatasetupload_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSetUpload(fbid=offlineconversiondatasetupload_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    offlineconversiondatasetupload_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSetUpload(fbid=offlineconversiondatasetupload_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    offlineconversiondatasetupload_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSetUpload(fbid=offlineconversiondatasetupload_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_progress(
    offlineconversiondatasetupload_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSetUpload(fbid=offlineconversiondatasetupload_id).get_progress(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_pull_sessions(
    offlineconversiondatasetupload_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineConversionDataSetUpload(
        fbid=offlineconversiondatasetupload_id
    ).get_pull_sessions(
        fields=fields,
        params=params,
    )

    return result


# Export the server
offlineconversiondatasetupload_server = mcp
