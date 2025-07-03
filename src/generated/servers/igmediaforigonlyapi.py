"""
Auto-generated MCP server for Facebook IGMediaForIGOnlyAPI.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igmediaforigonlyapi import IGMediaForIGOnlyAPI
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-igmediaforigonlyapi")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    igmediaforigonlyapi_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMediaForIGOnlyAPI(fbid=igmediaforigonlyapi_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    igmediaforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMediaForIGOnlyAPI(fbid=igmediaforigonlyapi_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    igmediaforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMediaForIGOnlyAPI(fbid=igmediaforigonlyapi_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    igmediaforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMediaForIGOnlyAPI(fbid=igmediaforigonlyapi_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_comment(
    igmediaforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMediaForIGOnlyAPI(fbid=igmediaforigonlyapi_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_children(
    igmediaforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMediaForIGOnlyAPI(fbid=igmediaforigonlyapi_id).get_children(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_comments(
    igmediaforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMediaForIGOnlyAPI(fbid=igmediaforigonlyapi_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_insights(
    igmediaforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGMediaForIGOnlyAPI(fbid=igmediaforigonlyapi_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igmediaforigonlyapi_server = mcp
