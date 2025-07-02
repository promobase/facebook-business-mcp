"""
Auto-generated MCP server for Facebook PagePost.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pagepost import PagePost
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-pagepost")


# CRUD Operations


@mcp.tool()
async def create_pagepost(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePost(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_pagepost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePost(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pagepost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePost(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_pagepost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePost(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_comment_for_pagepost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePost(fbid=object_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_like_for_pagepost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePost(fbid=object_id).create_like(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_likes_for_pagepost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePost(fbid=object_id).delete_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_attachments_for_pagepost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePost(fbid=object_id).get_attachments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_comments_for_pagepost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePost(fbid=object_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_dynamic_posts_for_pagepost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePost(fbid=object_id).get_dynamic_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_for_pagepost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePost(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_likes_for_pagepost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePost(fbid=object_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_reactions_for_pagepost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePost(fbid=object_id).get_reactions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shared_posts_for_pagepost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePost(fbid=object_id).get_shared_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_sponsor_tags_for_pagepost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePost(fbid=object_id).get_sponsor_tags(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_to_for_pagepost(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePost(fbid=object_id).get_to(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pagepost_server = mcp
