"""
Auto-generated MCP server for Facebook Canvas.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.canvas import Canvas
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-canvas")


# CRUD Operations


@mcp.tool()
async def get_canvas(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Canvas.

    Args:
        object_id: The ID of the Canvas
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Canvas(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_canvas(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a Canvas.

    Args:
        object_id: The ID of the Canvas
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = Canvas(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_pre_views_for_canvas(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Pre Views for Canvas.

    Args:
        object_id: The ID of the Canvas
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_pre_views result
    """
    result = Canvas(fbid=object_id).get_pre_views(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_preview_for_canvas(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Preview for Canvas.

    Args:
        object_id: The ID of the Canvas
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_preview result
    """
    result = Canvas(fbid=object_id).get_preview(
        fields=fields,
        params=params,
    )

    return result


# Export the server
canvas_server = mcp
