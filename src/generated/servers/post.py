"""Post MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.post import Post
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.comment import CommentField
from src.generated.models.insightsresult import InsightsResultField
from src.generated.models.post import (
    PostCreateCommentParams,
    PostCreateLikeParams,
    PostDeleteLikesParams,
    PostField,
    PostGetCommentsParams,
    PostGetInsightsParams,
    PostGetReactionsParams,
    PostUpdateParams,
)
from src.generated.models.profile import ProfileField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPost"
instructions = """
Post MCP Server for Facebook Business API.

Provides typed access to all Post operations.
"""

post_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@post_server.tool
@wrapped_fn_tool
def get_post(
    post_id: str,
    fields: list[PostField] = [],
) -> str:
    """Get a Post object by ID.

    Args:
        post_id: The ID of the Post.
        fields: Fields to retrieve. Available fields: See PostField type.
    """
    obj = Post(post_id)
    return obj.api_get(fields=fields)


@post_server.tool
@wrapped_fn_tool
def update_post(
    post_id: str,
    fields: list[PostField] = [],
    params: PostUpdateParams | dict = {},
) -> str:
    """Update a Post object.

    Args:
        post_id: The ID of the Post.
        fields: Fields to return after update. Available fields: See PostField type.
        params: Parameters to update. Available params: See PostUpdateParams type.
    """
    return Post(post_id).api_update(fields=fields, params=params)


@post_server.tool
@wrapped_fn_tool
def delete_post(
    post_id: str,
) -> str:
    """Delete a Post object.

    Args:
        post_id: The ID of the Post.
    """
    return Post(post_id).api_delete()


# ---- Edge Methods (6) ----
@post_server.tool
@wrapped_fn_tool
def get_comments(
    post_id: str,
    fields: list[CommentField] = [],
    params: PostGetCommentsParams | dict = {},
):
    """Get Comments for this Post.

    Args:
        post_id: The ID of the Post.
        fields: Fields to retrieve. Available fields: See CommentField type.
        params: Query parameters. Available params: See PostGetCommentsParams type.
    """
    return Post(post_id).get_comments(fields=fields, params=params)


@post_server.tool
@wrapped_fn_tool
def create_comment(
    post_id: str,
    fields: list[str] = [],
    params: PostCreateCommentParams | dict = {},
):
    """Create Comment for this Post.

    Args:
        post_id: The ID of the Post.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PostCreateCommentParams type.
    """
    return Post(post_id).create_comment(fields=fields, params=params)


@post_server.tool
@wrapped_fn_tool
def get_insights(
    post_id: str,
    fields: list[InsightsResultField] = [],
    params: PostGetInsightsParams | dict = {},
):
    """Get Insights for this Post.

    Args:
        post_id: The ID of the Post.
        fields: Fields to retrieve. Available fields: See InsightsResultField type.
        params: Query parameters. Available params: See PostGetInsightsParams type.
    """
    return Post(post_id).get_insights(fields=fields, params=params)


@post_server.tool
@wrapped_fn_tool
def delete_likes(
    post_id: str,
    params: PostDeleteLikesParams | dict = {},
):
    """Delete Likes for this Post.

    Args:
        post_id: The ID of the Post.
        params: Query parameters. Available params: See PostDeleteLikesParams type.
    """
    return Post(post_id).delete_likes(params=params)


@post_server.tool
@wrapped_fn_tool
def create_like(
    post_id: str,
    fields: list[str] = [],
    params: PostCreateLikeParams | dict = {},
):
    """Create Like for this Post.

    Args:
        post_id: The ID of the Post.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PostCreateLikeParams type.
    """
    return Post(post_id).create_like(fields=fields, params=params)


@post_server.tool
@wrapped_fn_tool
def get_reactions(
    post_id: str,
    fields: list[ProfileField] = [],
    params: PostGetReactionsParams | dict = {},
):
    """Get Reactions for this Post.

    Args:
        post_id: The ID of the Post.
        fields: Fields to retrieve. Available fields: See ProfileField type.
        params: Query parameters. Available params: See PostGetReactionsParams type.
    """
    return Post(post_id).get_reactions(fields=fields, params=params)
