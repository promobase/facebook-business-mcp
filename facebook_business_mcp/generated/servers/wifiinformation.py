"""
Auto-generated MCP server for Facebook WifiInformation.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.wifiinformation import WifiInformation
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-wifiinformation")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    wifiinformation_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WifiInformation(fbid=wifiinformation_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    wifiinformation_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WifiInformation(fbid=wifiinformation_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    wifiinformation_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WifiInformation(fbid=wifiinformation_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    wifiinformation_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WifiInformation(fbid=wifiinformation_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
wifiinformation_server = mcp
