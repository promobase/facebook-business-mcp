"""
Auto-generated MCP server for Facebook AudioRelease.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.audiorelease import AudioRelease
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-audiorelease")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    audiorelease_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AudioRelease(fbid=audiorelease_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    audiorelease_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AudioRelease(fbid=audiorelease_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    audiorelease_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AudioRelease(fbid=audiorelease_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    audiorelease_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AudioRelease(fbid=audiorelease_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
audiorelease_server = mcp
