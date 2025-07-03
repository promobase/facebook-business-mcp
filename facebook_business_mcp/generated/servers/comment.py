"""
Auto-generated MCP server for Facebook Comment.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.comment import Comment
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-comment")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    comment_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Comment(fbid=comment_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    comment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Comment(fbid=comment_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    comment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Comment(fbid=comment_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    comment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Comment(fbid=comment_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_comment(
    comment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Comment(fbid=comment_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_like(
    comment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Comment(fbid=comment_id).create_like(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_likes(
    comment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Comment(fbid=comment_id).delete_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_comments(
    comment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Comment(fbid=comment_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_likes(
    comment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Comment(fbid=comment_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_reactions(
    comment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Comment(fbid=comment_id).get_reactions(
        fields=fields,
        params=params,
    )

    return result


# Export the server
comment_server = mcp
