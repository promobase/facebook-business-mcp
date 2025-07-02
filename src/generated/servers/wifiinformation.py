"""
Auto-generated MCP server for Facebook WifiInformation.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.wifiinformation import WifiInformation
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-wifiinformation")


# CRUD Operations


@mcp.tool()
async def api_create_wifiinformation(
    wifiinformation_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WifiInformation(fbid=wifiinformation_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_wifiinformation(
    wifiinformation_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WifiInformation(fbid=wifiinformation_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_wifiinformation(
    wifiinformation_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WifiInformation(fbid=wifiinformation_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_wifiinformation(
    wifiinformation_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WifiInformation(fbid=wifiinformation_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
wifiinformation_server = mcp
