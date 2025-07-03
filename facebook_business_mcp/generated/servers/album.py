"""
Auto-generated MCP server for Facebook Album.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.album import Album
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-album")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    album_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Album(fbid=album_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    album_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Album(fbid=album_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    album_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Album(fbid=album_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    album_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Album(fbid=album_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_comment(
    album_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Album(fbid=album_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_like(
    album_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Album(fbid=album_id).create_like(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def create_photo(
    album_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Album(fbid=album_id).create_photo(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_comments(
    album_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Album(fbid=album_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_likes(
    album_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Album(fbid=album_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_photos(
    album_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Album(fbid=album_id).get_photos(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_picture(
    album_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Album(fbid=album_id).get_picture(
        fields=fields,
        params=params,
    )

    return result


# Export the server
album_server = mcp
