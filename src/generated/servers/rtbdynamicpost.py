"""
Auto-generated MCP server for Facebook RTBDynamicPost.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.rtbdynamicpost import RTBDynamicPost
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-rtbdynamicpost")


# CRUD Operations


@mcp.tool()
async def api_create_rtbdynamicpost(
    rtbdynamicpost_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = RTBDynamicPost(fbid=rtbdynamicpost_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_rtbdynamicpost(
    rtbdynamicpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = RTBDynamicPost(fbid=rtbdynamicpost_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_rtbdynamicpost(
    rtbdynamicpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = RTBDynamicPost(fbid=rtbdynamicpost_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_rtbdynamicpost(
    rtbdynamicpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = RTBDynamicPost(fbid=rtbdynamicpost_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_comments(
    rtbdynamicpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = RTBDynamicPost(fbid=rtbdynamicpost_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_likes(
    rtbdynamicpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = RTBDynamicPost(fbid=rtbdynamicpost_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


# Export the server
rtbdynamicpost_server = mcp
