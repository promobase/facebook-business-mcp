"""
Auto-generated MCP server for Facebook Canvas.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.canvas import Canvas
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-canvas")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    canvas_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Canvas(fbid=canvas_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    canvas_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Canvas(fbid=canvas_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    canvas_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Canvas(fbid=canvas_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    canvas_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Canvas(fbid=canvas_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_pre_views(
    canvas_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Canvas(fbid=canvas_id).get_pre_views(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_preview(
    canvas_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Canvas(fbid=canvas_id).get_preview(
        fields=fields,
        params=params,
    )

    return result


# Export the server
canvas_server = mcp
