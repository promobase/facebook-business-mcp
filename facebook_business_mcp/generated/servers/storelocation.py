"""
Auto-generated MCP server for Facebook StoreLocation.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.storelocation import StoreLocation
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-storelocation")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    storelocation_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = StoreLocation(fbid=storelocation_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    storelocation_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = StoreLocation(fbid=storelocation_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    storelocation_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = StoreLocation(fbid=storelocation_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    storelocation_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = StoreLocation(fbid=storelocation_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
storelocation_server = mcp
