"""
Auto-generated MCP server for Facebook WearableDevicePublicKey.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.wearabledevicepublickey import WearableDevicePublicKey
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-wearabledevicepublickey")


# CRUD Operations


@mcp.tool()
async def get_wearabledevicepublickey(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a WearableDevicePublicKey.

    Args:
        object_id: The ID of the WearableDevicePublicKey
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = WearableDevicePublicKey(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
wearabledevicepublickey_server = mcp
