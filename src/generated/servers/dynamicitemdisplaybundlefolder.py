"""
Auto-generated MCP server for Facebook DynamicItemDisplayBundleFolder.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.dynamicitemdisplaybundlefolder import (
    DynamicItemDisplayBundleFolder,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-dynamicitemdisplaybundlefolder")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    dynamicitemdisplaybundlefolder_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = DynamicItemDisplayBundleFolder(fbid=dynamicitemdisplaybundlefolder_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    dynamicitemdisplaybundlefolder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = DynamicItemDisplayBundleFolder(fbid=dynamicitemdisplaybundlefolder_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    dynamicitemdisplaybundlefolder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = DynamicItemDisplayBundleFolder(fbid=dynamicitemdisplaybundlefolder_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    dynamicitemdisplaybundlefolder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = DynamicItemDisplayBundleFolder(fbid=dynamicitemdisplaybundlefolder_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
dynamicitemdisplaybundlefolder_server = mcp
