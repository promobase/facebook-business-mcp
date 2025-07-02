"""
Auto-generated MCP server for Facebook BusinessVideo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessvideo import BusinessVideo
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessvideo")


# CRUD Operations


@mcp.tool()
async def api_create_businessvideo(
    businessvideo_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessVideo(fbid=businessvideo_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_businessvideo(
    businessvideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessVideo(fbid=businessvideo_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_businessvideo(
    businessvideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessVideo(fbid=businessvideo_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_businessvideo(
    businessvideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessVideo(fbid=businessvideo_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessvideo_server = mcp
