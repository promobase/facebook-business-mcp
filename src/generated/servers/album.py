"""Album MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.album import Album
from fastmcp import FastMCP

from src.generated.models.album import (
    AlbumCreateCommentParams,
    AlbumCreateLikeParams,
    AlbumCreatePhotoParams,
    AlbumField,
    AlbumGetCommentsParams,
    AlbumGetPictureParams,
)
from src.generated.models.comment import CommentField
from src.generated.models.photo import PhotoField
from src.generated.models.profilepicturesource import ProfilePictureSourceField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAlbum"
instructions = """
Album MCP Server for Facebook Business API.

Provides typed access to all Album operations.
"""

album_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@album_server.tool
@wrapped_fn_tool
def get_album(
    album_id: str,
    fields: list[AlbumField] = [],
) -> str:
    """Get a Album object by ID.

    Args:
        album_id: The ID of the Album.
        fields: Fields to retrieve. Available fields: See AlbumField type.
    """
    obj = Album(album_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (5) ----
@album_server.tool
@wrapped_fn_tool
def get_comments(
    album_id: str,
    fields: list[CommentField] = [],
    params: AlbumGetCommentsParams | dict = {},
):
    """Get Comments for this Album.

    Args:
        album_id: The ID of the Album.
        fields: Fields to retrieve. Available fields: See CommentField type.
        params: Query parameters. Available params: See AlbumGetCommentsParams type.
    """
    return Album(album_id).get_comments(fields=fields, params=params)


@album_server.tool
@wrapped_fn_tool
def create_comment(
    album_id: str,
    fields: list[str] = [],
    params: AlbumCreateCommentParams | dict = {},
):
    """Create Comment for this Album.

    Args:
        album_id: The ID of the Album.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AlbumCreateCommentParams type.
    """
    return Album(album_id).create_comment(fields=fields, params=params)


@album_server.tool
@wrapped_fn_tool
def create_like(
    album_id: str,
    fields: list[str] = [],
    params: AlbumCreateLikeParams | dict = {},
):
    """Create Like for this Album.

    Args:
        album_id: The ID of the Album.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AlbumCreateLikeParams type.
    """
    return Album(album_id).create_like(fields=fields, params=params)


@album_server.tool
@wrapped_fn_tool
def create_photo(
    album_id: str,
    fields: list[str] = [],
    params: AlbumCreatePhotoParams | dict = {},
):
    """Create Photo for this Album.

    Args:
        album_id: The ID of the Album.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AlbumCreatePhotoParams type.
    """
    return Album(album_id).create_photo(fields=fields, params=params)


@album_server.tool
@wrapped_fn_tool
def get_picture(
    album_id: str,
    fields: list[ProfilePictureSourceField] = [],
    params: AlbumGetPictureParams | dict = {},
):
    """Get Picture for this Album.

    Args:
        album_id: The ID of the Album.
        fields: Fields to retrieve. Available fields: See ProfilePictureSourceField type.
        params: Query parameters. Available params: See AlbumGetPictureParams type.
    """
    return Album(album_id).get_picture(fields=fields, params=params)
