"""LiveVideo MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.livevideo import LiveVideo
from fastmcp import FastMCP

from src.generated.models.comment import CommentField
from src.generated.models.livevideo import (
    LiveVideoCreatePollParams,
    LiveVideoField,
    LiveVideoGetBlockedUsersParams,
    LiveVideoGetCommentsParams,
    LiveVideoGetReactionsParams,
    LiveVideoUpdateParams,
)
from src.generated.models.profile import ProfileField
from src.generated.models.user import UserField
from src.generated.models.videopoll import VideoPollField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLiveVideo"
instructions = """
LiveVideo MCP Server for Facebook Business API.

Provides typed access to all LiveVideo operations.
"""

livevideo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@livevideo_server.tool
@wrapped_fn_tool
def get_livevideo(
    livevideo_id: str,
    fields: list[LiveVideoField] = [],
) -> str:
    """Get a LiveVideo object by ID.

    Args:
        livevideo_id: The ID of the LiveVideo.
        fields: Fields to retrieve. Available fields: See LiveVideoField type.
    """
    obj = LiveVideo(livevideo_id)
    return obj.api_get(fields=fields)


@livevideo_server.tool
@wrapped_fn_tool
def update_livevideo(
    livevideo_id: str,
    fields: list[LiveVideoField] = [],
    params: LiveVideoUpdateParams | dict = {},
) -> str:
    """Update a LiveVideo object.

    Args:
        livevideo_id: The ID of the LiveVideo.
        fields: Fields to return after update. Available fields: See LiveVideoField type.
        params: Parameters to update. Available params: See LiveVideoUpdateParams type.
    """
    return LiveVideo(livevideo_id).api_update(fields=fields, params=params)


@livevideo_server.tool
@wrapped_fn_tool
def delete_livevideo(
    livevideo_id: str,
) -> str:
    """Delete a LiveVideo object.

    Args:
        livevideo_id: The ID of the LiveVideo.
    """
    return LiveVideo(livevideo_id).api_delete()


# ---- Edge Methods (4) ----
@livevideo_server.tool
@wrapped_fn_tool
def get_blocked_users(
    livevideo_id: str,
    fields: list[UserField] = [],
    params: LiveVideoGetBlockedUsersParams | dict = {},
):
    """Get Blocked Users for this LiveVideo.

    Args:
        livevideo_id: The ID of the LiveVideo.
        fields: Fields to retrieve. Available fields: See UserField type.
        params: Query parameters. Available params: See LiveVideoGetBlockedUsersParams type.
    """
    return LiveVideo(livevideo_id).get_blocked_users(fields=fields, params=params)


@livevideo_server.tool
@wrapped_fn_tool
def get_comments(
    livevideo_id: str,
    fields: list[CommentField] = [],
    params: LiveVideoGetCommentsParams | dict = {},
):
    """Get Comments for this LiveVideo.

    Args:
        livevideo_id: The ID of the LiveVideo.
        fields: Fields to retrieve. Available fields: See CommentField type.
        params: Query parameters. Available params: See LiveVideoGetCommentsParams type.
    """
    return LiveVideo(livevideo_id).get_comments(fields=fields, params=params)


@livevideo_server.tool
@wrapped_fn_tool
def create_poll(
    livevideo_id: str,
    fields: list[str] = [],
    params: LiveVideoCreatePollParams | dict = {},
):
    """Create Poll for this LiveVideo.

    Args:
        livevideo_id: The ID of the LiveVideo.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See LiveVideoCreatePollParams type.
    """
    return LiveVideo(livevideo_id).create_poll(fields=fields, params=params)


@livevideo_server.tool
@wrapped_fn_tool
def get_reactions(
    livevideo_id: str,
    fields: list[ProfileField] = [],
    params: LiveVideoGetReactionsParams | dict = {},
):
    """Get Reactions for this LiveVideo.

    Args:
        livevideo_id: The ID of the LiveVideo.
        fields: Fields to retrieve. Available fields: See ProfileField type.
        params: Query parameters. Available params: See LiveVideoGetReactionsParams type.
    """
    return LiveVideo(livevideo_id).get_reactions(fields=fields, params=params)
