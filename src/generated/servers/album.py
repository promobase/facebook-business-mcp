"""
Auto-generated MCP server for Facebook Album.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.album import Album
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-album")


# CRUD Operations


@mcp.tool()
async def create_album(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Album(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_album(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Album(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_album(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Album(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_album(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Album(fbid=object_id).api_update(
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
    result = Album(fbid=object_id).get_picture(
        fields=fields,
        params=params,
    )

    return result


# Export the server
album_server = mcp
