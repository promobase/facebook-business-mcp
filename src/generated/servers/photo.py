"""Photo MCP Server with typed wrappers."""

from facebook_business.adobjects.photo import Photo
from fastmcp import FastMCP

from src.generated.models.comment import CommentField
from src.generated.models.insightsresult import InsightsResultField
from src.generated.models.photo import (
    PhotoCreateCommentParams,
    PhotoCreateLikeParams,
    PhotoField,
    PhotoGetCommentsParams,
    PhotoGetInsightsParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPhoto"
instructions = """
Photo MCP Server for Facebook Business API.

Provides typed access to all Photo operations.
"""

photo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@photo_server.tool
@wrapped_fn_tool
def get_photo(
    photo_id: str,
    fields: list[PhotoField] = [],
) -> str:
    """Get a Photo object by ID.

    Args:
        photo_id: The ID of the Photo.
        fields: Fields to retrieve. Available fields: See PhotoField type.
    """
    obj = Photo(photo_id)
    return obj.api_get(fields=fields)


@photo_server.tool
@wrapped_fn_tool
def delete_photo(
    photo_id: str,
) -> str:
    """Delete a Photo object.

    Args:
        photo_id: The ID of the Photo.
    """
    return Photo(photo_id).api_delete()


# ---- Edge Methods (4) ----
@photo_server.tool
@wrapped_fn_tool
def get_comments(
    photo_id: str,
    fields: list[CommentField] = [],
    params: PhotoGetCommentsParams | dict = {},
):
    """Get Comments for this Photo.

    Args:
        photo_id: The ID of the Photo.
        fields: Fields to retrieve. Available fields: See CommentField type.
        params: Query parameters. Available params: See PhotoGetCommentsParams type.
    """
    return Photo(photo_id).get_comments(fields=fields, params=params)


@photo_server.tool
@wrapped_fn_tool
def create_comment(
    photo_id: str,
    fields: list[str] = [],
    params: PhotoCreateCommentParams | dict = {},
):
    """Create Comment for this Photo.

    Args:
        photo_id: The ID of the Photo.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PhotoCreateCommentParams type.
    """
    return Photo(photo_id).create_comment(fields=fields, params=params)


@photo_server.tool
@wrapped_fn_tool
def get_insights(
    photo_id: str,
    fields: list[InsightsResultField] = [],
    params: PhotoGetInsightsParams | dict = {},
):
    """Get Insights for this Photo.

    Args:
        photo_id: The ID of the Photo.
        fields: Fields to retrieve. Available fields: See InsightsResultField type.
        params: Query parameters. Available params: See PhotoGetInsightsParams type.
    """
    return Photo(photo_id).get_insights(fields=fields, params=params)


@photo_server.tool
@wrapped_fn_tool
def create_like(
    photo_id: str,
    fields: list[str] = [],
    params: PhotoCreateLikeParams | dict = {},
):
    """Create Like for this Photo.

    Args:
        photo_id: The ID of the Photo.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PhotoCreateLikeParams type.
    """
    return Photo(photo_id).create_like(fields=fields, params=params)
