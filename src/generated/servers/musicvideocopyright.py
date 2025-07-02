"""
Auto-generated MCP server for Facebook MusicVideoCopyright.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.musicvideocopyright import MusicVideoCopyright
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-musicvideocopyright")


# CRUD Operations


@mcp.tool()
async def api_create_musicvideocopyright(
    musicvideocopyright_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MusicVideoCopyright(fbid=musicvideocopyright_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_musicvideocopyright(
    musicvideocopyright_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MusicVideoCopyright(fbid=musicvideocopyright_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_musicvideocopyright(
    musicvideocopyright_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MusicVideoCopyright(fbid=musicvideocopyright_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_musicvideocopyright(
    musicvideocopyright_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = MusicVideoCopyright(fbid=musicvideocopyright_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
musicvideocopyright_server = mcp
