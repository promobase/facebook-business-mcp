"""
Auto-generated MCP server for Facebook Post.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.post import Post
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-post")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    post_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Post(fbid=post_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Post(fbid=post_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Post(fbid=post_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Post(fbid=post_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_comment(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Post(fbid=post_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_like(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Post(fbid=post_id).create_like(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_likes(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Post(fbid=post_id).delete_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_attachments(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Post(fbid=post_id).get_attachments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_comments(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Post(fbid=post_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_dynamic_posts(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Post(fbid=post_id).get_dynamic_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_insights(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Post(fbid=post_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_reactions(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Post(fbid=post_id).get_reactions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_shared_posts(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Post(fbid=post_id).get_shared_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_sponsor_tags(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Post(fbid=post_id).get_sponsor_tags(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_to(
    post_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Post(fbid=post_id).get_to(
        fields=fields,
        params=params,
    )

    return result


# Export the server
post_server = mcp
