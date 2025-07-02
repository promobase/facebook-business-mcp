"""
Auto-generated MCP server for Facebook Album.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.album import Album
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-album")


# CRUD Operations


@mcp.tool()
async def get_album(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Album.

    Args:
        object_id: The ID of the Album
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Album(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_comment_for_album(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Comment for Album.

    Args:
        object_id: The ID of the Album
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_comment result
    """
    result = Album(fbid=object_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_like_for_album(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Like for Album.

    Args:
        object_id: The ID of the Album
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_like result
    """
    result = Album(fbid=object_id).create_like(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_photo_for_album(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Photo for Album.

    Args:
        object_id: The ID of the Album
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_photo result
    """
    result = Album(fbid=object_id).create_photo(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_comments_for_album(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Comments for Album.

    Args:
        object_id: The ID of the Album
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_comments result
    """
    result = Album(fbid=object_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_likes_for_album(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Likes for Album.

    Args:
        object_id: The ID of the Album
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_likes result
    """
    result = Album(fbid=object_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_photos_for_album(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Photos for Album.

    Args:
        object_id: The ID of the Album
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_photos result
    """
    result = Album(fbid=object_id).get_photos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_picture_for_album(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Picture for Album.

    Args:
        object_id: The ID of the Album
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_picture result
    """
    result = Album(fbid=object_id).get_picture(
        fields=fields,
        params=params,
    )

    return result


# Export the server
album_server = mcp
