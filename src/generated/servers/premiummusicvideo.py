"""
Auto-generated MCP server for Facebook PremiumMusicVideo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.premiummusicvideo import PremiumMusicVideo
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-premiummusicvideo")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    premiummusicvideo_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PremiumMusicVideo(fbid=premiummusicvideo_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    premiummusicvideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PremiumMusicVideo(fbid=premiummusicvideo_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    premiummusicvideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PremiumMusicVideo(fbid=premiummusicvideo_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    premiummusicvideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PremiumMusicVideo(fbid=premiummusicvideo_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
premiummusicvideo_server = mcp
