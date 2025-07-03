"""
Auto-generated MCP server for Facebook VideoCopyrightMatch.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.videocopyrightmatch import VideoCopyrightMatch
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-videocopyrightmatch")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    videocopyrightmatch_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoCopyrightMatch(fbid=videocopyrightmatch_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    videocopyrightmatch_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoCopyrightMatch(fbid=videocopyrightmatch_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    videocopyrightmatch_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoCopyrightMatch(fbid=videocopyrightmatch_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    videocopyrightmatch_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoCopyrightMatch(fbid=videocopyrightmatch_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
videocopyrightmatch_server = mcp
