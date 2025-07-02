"""
Auto-generated MCP server for Facebook Post.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.post import Post
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-post")


# CRUD Operations


@mcp.tool()
async def delete_post(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a Post.

    Args:
        object_id: The ID of the Post
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = Post(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_post(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Post.

    Args:
        object_id: The ID of the Post
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Post(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_post(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a Post.

    Args:
        object_id: The ID of the Post
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = Post(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_comment_for_post(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Comment for Post.

    Args:
        object_id: The ID of the Post
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_comment result
    """
    result = Post(fbid=object_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_like_for_post(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Like for Post.

    Args:
        object_id: The ID of the Post
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_like result
    """
    result = Post(fbid=object_id).create_like(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_likes_for_post(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Likes for Post.

    Args:
        object_id: The ID of the Post
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_likes result
    """
    result = Post(fbid=object_id).delete_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_attachments_for_post(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Attachments for Post.

    Args:
        object_id: The ID of the Post
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_attachments result
    """
    result = Post(fbid=object_id).get_attachments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_comments_for_post(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Comments for Post.

    Args:
        object_id: The ID of the Post
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_comments result
    """
    result = Post(fbid=object_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_dynamic_posts_for_post(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Dynamic Posts for Post.

    Args:
        object_id: The ID of the Post
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_dynamic_posts result
    """
    result = Post(fbid=object_id).get_dynamic_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_for_post(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Insights for Post.

    Args:
        object_id: The ID of the Post
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights result
    """
    result = Post(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_reactions_for_post(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Reactions for Post.

    Args:
        object_id: The ID of the Post
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_reactions result
    """
    result = Post(fbid=object_id).get_reactions(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shared_posts_for_post(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Shared Posts for Post.

    Args:
        object_id: The ID of the Post
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_shared_posts result
    """
    result = Post(fbid=object_id).get_shared_posts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_sponsor_tags_for_post(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Sponsor Tags for Post.

    Args:
        object_id: The ID of the Post
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_sponsor_tags result
    """
    result = Post(fbid=object_id).get_sponsor_tags(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_to_for_post(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get To for Post.

    Args:
        object_id: The ID of the Post
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_to result
    """
    result = Post(fbid=object_id).get_to(
        fields=fields,
        params=params,
    )

    return result


# Export the server
post_server = mcp
