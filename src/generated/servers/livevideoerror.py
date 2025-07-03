"""
Auto-generated MCP server for Facebook LiveVideoError.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.livevideoerror import LiveVideoError
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-livevideoerror")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    livevideoerror_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideoError(fbid=livevideoerror_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    livevideoerror_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideoError(fbid=livevideoerror_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    livevideoerror_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideoError(fbid=livevideoerror_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    livevideoerror_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideoError(fbid=livevideoerror_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
livevideoerror_server = mcp
