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
async def create_rtbdynamicpost(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = RTBDynamicPost(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_rtbdynamicpost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = RTBDynamicPost(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_rtbdynamicpost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = RTBDynamicPost(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_rtbdynamicpost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = RTBDynamicPost(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_comments_for_rtbdynamicpost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = RTBDynamicPost(fbid=object_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_likes_for_rtbdynamicpost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = RTBDynamicPost(fbid=object_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


# Export the server
rtbdynamicpost_server = mcp
