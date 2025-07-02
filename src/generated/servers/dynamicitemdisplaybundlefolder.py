"""
Auto-generated MCP server for Facebook DynamicItemDisplayBundleFolder.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.dynamicitemdisplaybundlefolder import (
    DynamicItemDisplayBundleFolder,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-dynamicitemdisplaybundlefolder")


# CRUD Operations


@mcp.tool()
async def create_dynamicitemdisplaybundlefolder(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DynamicItemDisplayBundleFolder(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_dynamicitemdisplaybundlefolder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DynamicItemDisplayBundleFolder(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_dynamicitemdisplaybundlefolder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DynamicItemDisplayBundleFolder(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_dynamicitemdisplaybundlefolder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = DynamicItemDisplayBundleFolder(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
dynamicitemdisplaybundlefolder_server = mcp
