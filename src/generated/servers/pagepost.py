"""PagePost MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.pagepost import PagePost
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.comment import CommentField
from src.generated.models.insightsresult import InsightsResultField
from src.generated.models.pagepost import (
    PagePostCreateCommentParams,
    PagePostCreateLikeParams,
    PagePostDeleteLikesParams,
    PagePostField,
    PagePostGetCommentsParams,
    PagePostGetInsightsParams,
    PagePostGetReactionsParams,
    PagePostUpdateParams,
)
from src.generated.models.profile import ProfileField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPagePost"
instructions = """
PagePost MCP Server for Facebook Business API.

Provides typed access to all PagePost operations.
"""

pagepost_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@pagepost_server.tool
@wrapped_fn_tool
def get_pagepost(
    pagepost_id: str,
    fields: list[PagePostField] = [],
) -> str:
    """Get a PagePost object by ID.

    Args:
        pagepost_id: The ID of the PagePost.
        fields: Fields to retrieve. Available fields: See PagePostField type.
    """
    obj = PagePost(pagepost_id)
    return obj.api_get(fields=fields)


@pagepost_server.tool
@wrapped_fn_tool
def update_pagepost(
    pagepost_id: str,
    fields: list[PagePostField] = [],
    params: PagePostUpdateParams | dict = {},
) -> str:
    """Update a PagePost object.

    Args:
        pagepost_id: The ID of the PagePost.
        fields: Fields to return after update. Available fields: See PagePostField type.
        params: Parameters to update. Available params: See PagePostUpdateParams type.
    """
    return PagePost(pagepost_id).api_update(fields=fields, params=params)


@pagepost_server.tool
@wrapped_fn_tool
def delete_pagepost(
    pagepost_id: str,
) -> str:
    """Delete a PagePost object.

    Args:
        pagepost_id: The ID of the PagePost.
    """
    return PagePost(pagepost_id).api_delete()


# ---- Edge Methods (6) ----
@pagepost_server.tool
@wrapped_fn_tool
def get_comments(
    pagepost_id: str,
    fields: list[CommentField] = [],
    params: PagePostGetCommentsParams | dict = {},
):
    """Get Comments for this PagePost.

    Args:
        pagepost_id: The ID of the PagePost.
        fields: Fields to retrieve. Available fields: See CommentField type.
        params: Query parameters. Available params: See PagePostGetCommentsParams type.
    """
    return PagePost(pagepost_id).get_comments(fields=fields, params=params)


@pagepost_server.tool
@wrapped_fn_tool
def create_comment(
    pagepost_id: str,
    fields: list[str] = [],
    params: PagePostCreateCommentParams | dict = {},
):
    """Create Comment for this PagePost.

    Args:
        pagepost_id: The ID of the PagePost.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PagePostCreateCommentParams type.
    """
    return PagePost(pagepost_id).create_comment(fields=fields, params=params)


@pagepost_server.tool
@wrapped_fn_tool
def get_insights(
    pagepost_id: str,
    fields: list[InsightsResultField] = [],
    params: PagePostGetInsightsParams | dict = {},
):
    """Get Insights for this PagePost.

    Args:
        pagepost_id: The ID of the PagePost.
        fields: Fields to retrieve. Available fields: See InsightsResultField type.
        params: Query parameters. Available params: See PagePostGetInsightsParams type.
    """
    return PagePost(pagepost_id).get_insights(fields=fields, params=params)


@pagepost_server.tool
@wrapped_fn_tool
def delete_likes(
    pagepost_id: str,
    params: PagePostDeleteLikesParams | dict = {},
):
    """Delete Likes for this PagePost.

    Args:
        pagepost_id: The ID of the PagePost.
        params: Query parameters. Available params: See PagePostDeleteLikesParams type.
    """
    return PagePost(pagepost_id).delete_likes(params=params)


@pagepost_server.tool
@wrapped_fn_tool
def create_like(
    pagepost_id: str,
    fields: list[str] = [],
    params: PagePostCreateLikeParams | dict = {},
):
    """Create Like for this PagePost.

    Args:
        pagepost_id: The ID of the PagePost.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PagePostCreateLikeParams type.
    """
    return PagePost(pagepost_id).create_like(fields=fields, params=params)


@pagepost_server.tool
@wrapped_fn_tool
def get_reactions(
    pagepost_id: str,
    fields: list[ProfileField] = [],
    params: PagePostGetReactionsParams | dict = {},
):
    """Get Reactions for this PagePost.

    Args:
        pagepost_id: The ID of the PagePost.
        fields: Fields to retrieve. Available fields: See ProfileField type.
        params: Query parameters. Available params: See PagePostGetReactionsParams type.
    """
    return PagePost(pagepost_id).get_reactions(fields=fields, params=params)
