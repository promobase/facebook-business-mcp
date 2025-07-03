"""
Auto-generated MCP server for Facebook BusinessVideo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessvideo import BusinessVideo
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-businessvideo")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    businessvideo_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessVideo(fbid=businessvideo_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    businessvideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessVideo(fbid=businessvideo_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    businessvideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessVideo(fbid=businessvideo_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    businessvideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessVideo(fbid=businessvideo_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessvideo_server = mcp
