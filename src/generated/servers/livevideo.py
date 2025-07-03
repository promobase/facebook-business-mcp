"""
Auto-generated MCP server for Facebook LiveVideo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.livevideo import LiveVideo
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-livevideo")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    livevideo_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideo(fbid=livevideo_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideo(fbid=livevideo_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideo(fbid=livevideo_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideo(fbid=livevideo_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_input_stream(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideo(fbid=livevideo_id).create_input_stream(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_poll(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideo(fbid=livevideo_id).create_poll(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_blocked_users(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideo(fbid=livevideo_id).get_blocked_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_comments(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideo(fbid=livevideo_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_crosspost_shared_pages(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideo(fbid=livevideo_id).get_crosspost_shared_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_crossposted_broadcasts(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideo(fbid=livevideo_id).get_crossposted_broadcasts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_errors(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideo(fbid=livevideo_id).get_errors(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_polls(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideo(fbid=livevideo_id).get_polls(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_reactions(
    livevideo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = LiveVideo(fbid=livevideo_id).get_reactions(
        fields=fields,
        params=params,
    )

    return result


# Export the server
livevideo_server = mcp
