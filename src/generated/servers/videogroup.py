"""
Auto-generated MCP server for Facebook VideoGroup.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.videogroup import VideoGroup
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-videogroup")


# CRUD Operations


@mcp.tool()
async def api_create_videogroup(
    videogroup_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = VideoGroup(fbid=videogroup_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_videogroup(
    videogroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = VideoGroup(fbid=videogroup_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_videogroup(
    videogroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = VideoGroup(fbid=videogroup_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_videogroup(
    videogroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = VideoGroup(fbid=videogroup_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
videogroup_server = mcp
