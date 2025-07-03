"""
Auto-generated MCP server for Facebook WITUser.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.wituser import WITUser
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-wituser")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    wituser_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WITUser(fbid=wituser_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    wituser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WITUser(fbid=wituser_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    wituser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WITUser(fbid=wituser_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    wituser_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WITUser(fbid=wituser_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
wituser_server = mcp
