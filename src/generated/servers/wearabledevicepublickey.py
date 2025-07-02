"""
Auto-generated MCP server for Facebook WearableDevicePublicKey.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.wearabledevicepublickey import WearableDevicePublicKey
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-wearabledevicepublickey")


# CRUD Operations


@mcp.tool()
async def create_wearabledevicepublickey(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WearableDevicePublicKey(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_wearabledevicepublickey(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WearableDevicePublicKey(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_wearabledevicepublickey(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WearableDevicePublicKey(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_wearabledevicepublickey(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WearableDevicePublicKey(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
wearabledevicepublickey_server = mcp
