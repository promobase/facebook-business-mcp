"""
Auto-generated MCP server for Facebook Comment.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.comment import Comment
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-comment")


# CRUD Operations


@mcp.tool()
async def create_comment(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Comment(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_comment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Comment(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_comment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Comment(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_comment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Comment(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_comment_for_comment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Comment(fbid=object_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_like_for_comment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Comment(fbid=object_id).create_like(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_likes_for_comment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Comment(fbid=object_id).delete_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_comments_for_comment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Comment(fbid=object_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_likes_for_comment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Comment(fbid=object_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_reactions_for_comment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Comment(fbid=object_id).get_reactions(
        fields=fields,
        params=params,
    )

    return result


# Export the server
comment_server = mcp
