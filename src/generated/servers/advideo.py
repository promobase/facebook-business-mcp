"""AdVideo MCP Server with typed wrappers."""

from __future__ import annotations

from typing import Any

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
@wrapped_fn_tool
def get_advideo(
    advideo_id: str,
    fields: list[AdVideoField] = [],
) -> str:
    """Get a AdVideo object by ID.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
    """
    obj = AdVideo(advideo_id)
    return obj.api_get(fields=fields)


advideo_server.tool(get_advideo)


@wrapped_fn_tool
def update_advideo(
    advideo_id: str,
    fields: list[AdVideoField] = [],
    params: AdVideoUpdateParams | dict[str, Any] = {},
) -> str:
    """Update a AdVideo object.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to return after update.
        params: Parameters to update.
    """
    return AdVideo(advideo_id).api_update(fields=fields, params=params)


advideo_server.tool(update_advideo)


@wrapped_fn_tool
def delete_advideo(
    advideo_id: str,
) -> str:
    """Delete a AdVideo object.

    Args:
        advideo_id: The ID of the AdVideo.
    """
    return AdVideo(advideo_id).api_delete()


advideo_server.tool(delete_advideo)


# ---- Edge Methods (9) ----
@wrapped_fn_tool
def create_cap_t_i_on(
    advideo_id: str,
    fields: list[str] = [],
    params: AdVideoCreateCapTIOnParams = {},
) -> Any:
    """Create Cap T I On for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdVideo(advideo_id).create_cap_t_i_on(fields=fields, params=params)


advideo_server.tool(create_cap_t_i_on)


@wrapped_fn_tool
def create_collaborator(
    advideo_id: str,
    fields: list[str] = [],
    params: AdVideoCreateCollaboratorParams = {},
) -> Any:
    """Create Collaborator for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdVideo(advideo_id).create_collaborator(fields=fields, params=params)


advideo_server.tool(create_collaborator)


@wrapped_fn_tool
def get_comments(
    advideo_id: str,
    fields: list[CommentField] = [],
    params: AdVideoGetCommentsParams = {},
) -> Any:
    """Get Comments for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdVideo(advideo_id).get_comments(fields=fields, params=params)


advideo_server.tool(get_comments)


@wrapped_fn_tool
def create_comment(
    advideo_id: str,
    fields: list[str] = [],
    params: AdVideoCreateCommentParams = {},
) -> Any:
    """Create Comment for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdVideo(advideo_id).create_comment(fields=fields, params=params)


advideo_server.tool(create_comment)


@wrapped_fn_tool
def create_gaming_clip_create(
    advideo_id: str,
    fields: list[str] = [],
    params: AdVideoCreateGamingClipCreateParams = {},
) -> Any:
    """Create Gaming Clip Create for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdVideo(advideo_id).create_gaming_clip_create(fields=fields, params=params)


advideo_server.tool(create_gaming_clip_create)


@wrapped_fn_tool
def create_like(
    advideo_id: str,
    fields: list[str] = [],
    params: AdVideoCreateLikeParams = {},
) -> Any:
    """Create Like for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdVideo(advideo_id).create_like(fields=fields, params=params)


advideo_server.tool(create_like)


@wrapped_fn_tool
def create_poll(
    advideo_id: str,
    fields: list[str] = [],
    params: AdVideoCreatePollParams = {},
) -> Any:
    """Create Poll for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdVideo(advideo_id).create_poll(fields=fields, params=params)


advideo_server.tool(create_poll)


@wrapped_fn_tool
def create_thumbnail(
    advideo_id: str,
    fields: list[str] = [],
    params: AdVideoCreateThumbnailParams = {},
) -> Any:
    """Create Thumbnail for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdVideo(advideo_id).create_thumbnail(fields=fields, params=params)


advideo_server.tool(create_thumbnail)


@wrapped_fn_tool
def get_video_insights(
    advideo_id: str,
    fields: list[InsightsResultField] = [],
    params: AdVideoGetVideoInsightsParams = {},
) -> Any:
    """Get Video Insights for this AdVideo.

    Args:
        advideo_id: The ID of the AdVideo.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdVideo(advideo_id).get_video_insights(fields=fields, params=params)


advideo_server.tool(get_video_insights)
