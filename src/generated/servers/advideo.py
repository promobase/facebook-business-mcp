"""AdVideo MCP Server with typed wrappers."""

from facebook_business.adobjects.advideo import AdVideo
from fastmcp import FastMCP

from src.generated.models.advideo import (
    AdVideoCreateCapTIOnParams,
    AdVideoCreateCollaboratorParams,
    AdVideoCreateCommentParams,
    AdVideoCreateGamingClipCreateParams,
    AdVideoCreateLikeParams,
    AdVideoCreatePollParams,
    AdVideoCreateThumbnailParams,
    AdVideoField,
    AdVideoGetCommentsParams,
    AdVideoGetVideoInsightsParams,
    AdVideoUpdateParams,
)
from src.generated.models.comment import CommentField
from src.generated.models.insightsresult import InsightsResultField
from src.generated.models.videopoll import VideoPollField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdVideo"
instructions = """
AdVideo MCP Server for Facebook Business API.

Provides typed access to all AdVideo operations.
"""

advideo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@advideo_server.tool
@wrapped_fn_tool
def get_advideo(
    advideo_id: str,
    fields: list[AdVideoField] = [],
) -> str:
    """Get a AdVideo object by ID.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve. Available fields: See AdVideoField type.
    """
    obj = AdVideo(advideo_id)
    return obj.api_get(fields=fields)


@advideo_server.tool
@wrapped_fn_tool
def update_advideo(
    advideo_id: str,
    fields: list[AdVideoField] = [],
    params: AdVideoUpdateParams | dict = {},
) -> str:
    """Update a AdVideo object.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to return after update. Available fields: See AdVideoField type.
        params: Parameters to update. Available params: See AdVideoUpdateParams type.
    """
    return AdVideo(advideo_id).api_update(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def delete_advideo(
    advideo_id: str,
) -> str:
    """Delete a AdVideo object.

    Args:
        advideo_id: The ID of the AdVideo.
    """
    return AdVideo(advideo_id).api_delete()


# ---- Edge Methods (9) ----
@advideo_server.tool
@wrapped_fn_tool
def create_cap_t_i_on(
    advideo_id: str,
    fields: list[str] = [],
    params: AdVideoCreateCapTIOnParams | dict = {},
):
    """Create Cap T I On for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdVideoCreateCapTIOnParams type.
    """
    return AdVideo(advideo_id).create_cap_t_i_on(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def create_collaborator(
    advideo_id: str,
    fields: list[str] = [],
    params: AdVideoCreateCollaboratorParams | dict = {},
):
    """Create Collaborator for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdVideoCreateCollaboratorParams type.
    """
    return AdVideo(advideo_id).create_collaborator(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def get_comments(
    advideo_id: str,
    fields: list[CommentField] = [],
    params: AdVideoGetCommentsParams | dict = {},
):
    """Get Comments for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve. Available fields: See CommentField type.
        params: Query parameters. Available params: See AdVideoGetCommentsParams type.
    """
    return AdVideo(advideo_id).get_comments(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def create_comment(
    advideo_id: str,
    fields: list[str] = [],
    params: AdVideoCreateCommentParams | dict = {},
):
    """Create Comment for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdVideoCreateCommentParams type.
    """
    return AdVideo(advideo_id).create_comment(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def create_gaming_clip_create(
    advideo_id: str,
    fields: list[str] = [],
    params: AdVideoCreateGamingClipCreateParams | dict = {},
):
    """Create Gaming Clip Create for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdVideoCreateGamingClipCreateParams type.
    """
    return AdVideo(advideo_id).create_gaming_clip_create(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def create_like(
    advideo_id: str,
    fields: list[str] = [],
    params: AdVideoCreateLikeParams | dict = {},
):
    """Create Like for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdVideoCreateLikeParams type.
    """
    return AdVideo(advideo_id).create_like(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def create_poll(
    advideo_id: str,
    fields: list[str] = [],
    params: AdVideoCreatePollParams | dict = {},
):
    """Create Poll for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdVideoCreatePollParams type.
    """
    return AdVideo(advideo_id).create_poll(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def create_thumbnail(
    advideo_id: str,
    fields: list[str] = [],
    params: AdVideoCreateThumbnailParams | dict = {},
):
    """Create Thumbnail for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdVideoCreateThumbnailParams type.
    """
    return AdVideo(advideo_id).create_thumbnail(fields=fields, params=params)


@advideo_server.tool
@wrapped_fn_tool
def get_video_insights(
    advideo_id: str,
    fields: list[InsightsResultField] = [],
    params: AdVideoGetVideoInsightsParams | dict = {},
):
    """Get Video Insights for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve. Available fields: See InsightsResultField type.
        params: Query parameters. Available params: See AdVideoGetVideoInsightsParams type.
    """
    return AdVideo(advideo_id).get_video_insights(fields=fields, params=params)
