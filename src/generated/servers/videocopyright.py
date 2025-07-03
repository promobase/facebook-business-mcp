"""
Auto-generated MCP server for Facebook VideoCopyright.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.videocopyright import VideoCopyright
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-videocopyright")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    videocopyright_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoCopyright(fbid=videocopyright_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    videocopyright_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoCopyright(fbid=videocopyright_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    videocopyright_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoCopyright(fbid=videocopyright_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    videocopyright_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoCopyright(fbid=videocopyright_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_update_records(
    videocopyright_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoCopyright(fbid=videocopyright_id).get_update_records(
        fields=fields,
        params=params,
    )

    return result


# Export the server
videocopyright_server = mcp
