"""
Auto-generated MCP server for Facebook Photo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.photo import Photo
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-photo")


# CRUD Operations


@mcp.tool()
async def api_create_photo(
    photo_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Photo(fbid=photo_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_photo(
    photo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Photo(fbid=photo_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_photo(
    photo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Photo(fbid=photo_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_photo(
    photo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Photo(fbid=photo_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_comment(
    photo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Photo(fbid=photo_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_like(
    photo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Photo(fbid=photo_id).create_like(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_comments(
    photo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Photo(fbid=photo_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights(
    photo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Photo(fbid=photo_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_likes(
    photo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Photo(fbid=photo_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_sponsor_tags(
    photo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Photo(fbid=photo_id).get_sponsor_tags(
        fields=fields,
        params=params,
    )

    return result


# Export the server
photo_server = mcp
