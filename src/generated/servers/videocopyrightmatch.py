"""
Auto-generated MCP server for Facebook VideoCopyrightMatch.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.videocopyrightmatch import VideoCopyrightMatch
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-videocopyrightmatch")


# CRUD Operations


@mcp.tool()
async def api_create_videocopyrightmatch(
    videocopyrightmatch_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = VideoCopyrightMatch(fbid=videocopyrightmatch_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_videocopyrightmatch(
    videocopyrightmatch_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = VideoCopyrightMatch(fbid=videocopyrightmatch_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_videocopyrightmatch(
    videocopyrightmatch_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = VideoCopyrightMatch(fbid=videocopyrightmatch_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_videocopyrightmatch(
    videocopyrightmatch_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = VideoCopyrightMatch(fbid=videocopyrightmatch_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
videocopyrightmatch_server = mcp
