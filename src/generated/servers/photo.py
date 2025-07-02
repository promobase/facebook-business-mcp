"""
Auto-generated MCP server for Facebook Photo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.photo import Photo
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-photo")


# CRUD Operations


@mcp.tool()
async def delete_photo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a Photo.

    Args:
        object_id: The ID of the Photo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = Photo(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_photo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Photo.

    Args:
        object_id: The ID of the Photo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Photo(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_comment_for_photo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Comment for Photo.

    Args:
        object_id: The ID of the Photo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_comment result
    """
    result = Photo(fbid=object_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_like_for_photo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Like for Photo.

    Args:
        object_id: The ID of the Photo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_like result
    """
    result = Photo(fbid=object_id).create_like(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_comments_for_photo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Comments for Photo.

    Args:
        object_id: The ID of the Photo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_comments result
    """
    result = Photo(fbid=object_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_for_photo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Insights for Photo.

    Args:
        object_id: The ID of the Photo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights result
    """
    result = Photo(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_likes_for_photo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Likes for Photo.

    Args:
        object_id: The ID of the Photo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_likes result
    """
    result = Photo(fbid=object_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_sponsor_tags_for_photo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Sponsor Tags for Photo.

    Args:
        object_id: The ID of the Photo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_sponsor_tags result
    """
    result = Photo(fbid=object_id).get_sponsor_tags(
        fields=fields,
        params=params,
    )

    return result


# Export the server
photo_server = mcp
