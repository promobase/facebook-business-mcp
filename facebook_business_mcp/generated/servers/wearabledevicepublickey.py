"""
Auto-generated MCP server for Facebook WearableDevicePublicKey.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.wearabledevicepublickey import WearableDevicePublicKey
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-wearabledevicepublickey")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    wearabledevicepublickey_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WearableDevicePublicKey(fbid=wearabledevicepublickey_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    wearabledevicepublickey_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WearableDevicePublicKey(fbid=wearabledevicepublickey_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    wearabledevicepublickey_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WearableDevicePublicKey(fbid=wearabledevicepublickey_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    wearabledevicepublickey_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WearableDevicePublicKey(fbid=wearabledevicepublickey_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
wearabledevicepublickey_server = mcp
