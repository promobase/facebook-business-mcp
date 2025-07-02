"""
Auto-generated MCP server for Facebook IGMediaForIGOnlyAPI.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igmediaforigonlyapi import IGMediaForIGOnlyAPI
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-igmediaforigonlyapi")


# CRUD Operations


@mcp.tool()
async def create_igmediaforigonlyapi(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGMediaForIGOnlyAPI(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_igmediaforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGMediaForIGOnlyAPI(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_igmediaforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGMediaForIGOnlyAPI(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_igmediaforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGMediaForIGOnlyAPI(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_comment_for_igmediaforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGMediaForIGOnlyAPI(fbid=object_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_children_for_igmediaforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGMediaForIGOnlyAPI(fbid=object_id).get_children(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_comments_for_igmediaforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGMediaForIGOnlyAPI(fbid=object_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_for_igmediaforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGMediaForIGOnlyAPI(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igmediaforigonlyapi_server = mcp
