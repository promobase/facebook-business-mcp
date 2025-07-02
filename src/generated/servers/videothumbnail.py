"""
Auto-generated MCP server for Facebook VideoThumbnail.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.videothumbnail import VideoThumbnail
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-videothumbnail")


# CRUD Operations


@mcp.tool()
async def api_create_videothumbnail(
    videothumbnail_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = VideoThumbnail(fbid=videothumbnail_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_videothumbnail(
    videothumbnail_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = VideoThumbnail(fbid=videothumbnail_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_videothumbnail(
    videothumbnail_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = VideoThumbnail(fbid=videothumbnail_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_videothumbnail(
    videothumbnail_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = VideoThumbnail(fbid=videothumbnail_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
videothumbnail_server = mcp
