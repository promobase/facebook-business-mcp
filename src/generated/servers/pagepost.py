"""
Auto-generated MCP server for Facebook PagePost.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pagepost import PagePost
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-pagepost")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    pagepost_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePost(fbid=pagepost_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePost(fbid=pagepost_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePost(fbid=pagepost_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePost(fbid=pagepost_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_comment(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePost(fbid=pagepost_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_like(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePost(fbid=pagepost_id).create_like(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def delete_likes(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePost(fbid=pagepost_id).delete_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_attachments(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePost(fbid=pagepost_id).get_attachments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_comments(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePost(fbid=pagepost_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_dynamic_posts(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePost(fbid=pagepost_id).get_dynamic_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_insights(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePost(fbid=pagepost_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_likes(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePost(fbid=pagepost_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_reactions(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePost(fbid=pagepost_id).get_reactions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_shared_posts(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePost(fbid=pagepost_id).get_shared_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_sponsor_tags(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePost(fbid=pagepost_id).get_sponsor_tags(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_to(
    pagepost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = PagePost(fbid=pagepost_id).get_to(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pagepost_server = mcp
