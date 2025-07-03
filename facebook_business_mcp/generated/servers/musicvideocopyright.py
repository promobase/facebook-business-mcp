"""
Auto-generated MCP server for Facebook MusicVideoCopyright.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.musicvideocopyright import MusicVideoCopyright
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-musicvideocopyright")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    musicvideocopyright_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MusicVideoCopyright(fbid=musicvideocopyright_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    musicvideocopyright_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MusicVideoCopyright(fbid=musicvideocopyright_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    musicvideocopyright_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MusicVideoCopyright(fbid=musicvideocopyright_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    musicvideocopyright_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MusicVideoCopyright(fbid=musicvideocopyright_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
musicvideocopyright_server = mcp
