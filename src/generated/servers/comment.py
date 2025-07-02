"""Comment MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.comment import Comment
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.comment import (
    CommentCreateCommentParams,
    CommentCreateLikeParams,
    CommentDeleteLikesParams,
    CommentField,
    CommentGetCommentsParams,
    CommentGetReactionsParams,
    CommentUpdateParams,
)
from src.generated.models.profile import ProfileField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookComment"
instructions = """
Comment MCP Server for Facebook Business API.

Provides typed access to all Comment operations.
"""

comment_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@comment_server.tool
@wrapped_fn_tool
def get_comment(
    comment_id: str,
    fields: list[CommentField] = [],
) -> str:
    """Get a Comment object by ID.

    Args:
        comment_id: The ID of the Comment.
        fields: Fields to retrieve. Available fields: See CommentField type.
    """
    obj = Comment(comment_id)
    return obj.api_get(fields=fields)


@comment_server.tool
@wrapped_fn_tool
def update_comment(
    comment_id: str,
    fields: list[CommentField] = [],
    params: CommentUpdateParams | dict = {},
) -> str:
    """Update a Comment object.

    Args:
        comment_id: The ID of the Comment.
        fields: Fields to return after update. Available fields: See CommentField type.
        params: Parameters to update. Available params: See CommentUpdateParams type.
    """
    return Comment(comment_id).api_update(fields=fields, params=params)


@comment_server.tool
@wrapped_fn_tool
def delete_comment(
    comment_id: str,
) -> str:
    """Delete a Comment object.

    Args:
        comment_id: The ID of the Comment.
    """
    return Comment(comment_id).api_delete()


# ---- Edge Methods (5) ----
@comment_server.tool
@wrapped_fn_tool
def get_comments(
    comment_id: str,
    fields: list[CommentField] = [],
    params: CommentGetCommentsParams | dict = {},
):
    """Get Comments for this Comment.

    Args:
        comment_id: The ID of the Comment.
        fields: Fields to retrieve. Available fields: See CommentField type.
        params: Query parameters. Available params: See CommentGetCommentsParams type.
    """
    return Comment(comment_id).get_comments(fields=fields, params=params)


@comment_server.tool
@wrapped_fn_tool
def create_comment(
    comment_id: str,
    fields: list[str] = [],
    params: CommentCreateCommentParams | dict = {},
):
    """Create Comment for this Comment.

    Args:
        comment_id: The ID of the Comment.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CommentCreateCommentParams type.
    """
    return Comment(comment_id).create_comment(fields=fields, params=params)


@comment_server.tool
@wrapped_fn_tool
def delete_likes(
    comment_id: str,
    params: CommentDeleteLikesParams | dict = {},
):
    """Delete Likes for this Comment.

    Args:
        comment_id: The ID of the Comment.
        params: Query parameters. Available params: See CommentDeleteLikesParams type.
    """
    return Comment(comment_id).delete_likes(params=params)


@comment_server.tool
@wrapped_fn_tool
def create_like(
    comment_id: str,
    fields: list[str] = [],
    params: CommentCreateLikeParams | dict = {},
):
    """Create Like for this Comment.

    Args:
        comment_id: The ID of the Comment.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CommentCreateLikeParams type.
    """
    return Comment(comment_id).create_like(fields=fields, params=params)


@comment_server.tool
@wrapped_fn_tool
def get_reactions(
    comment_id: str,
    fields: list[ProfileField] = [],
    params: CommentGetReactionsParams | dict = {},
):
    """Get Reactions for this Comment.

    Args:
        comment_id: The ID of the Comment.
        fields: Fields to retrieve. Available fields: See ProfileField type.
        params: Query parameters. Available params: See CommentGetReactionsParams type.
    """
    return Comment(comment_id).get_reactions(fields=fields, params=params)
