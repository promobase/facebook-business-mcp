"""
Auto-generated MCP server for Facebook VideoList.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.videolist import VideoList
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-videolist")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    videolist_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoList(fbid=videolist_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    videolist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoList(fbid=videolist_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    videolist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoList(fbid=videolist_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    videolist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoList(fbid=videolist_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_videos(
    videolist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoList(fbid=videolist_id).get_videos(
        fields=fields,
        params=params,
    )

    return result


# Export the server
videolist_server = mcp
