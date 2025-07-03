"""
Auto-generated MCP server for Facebook Link.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.link import Link
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-link")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    link_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Link(fbid=link_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    link_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Link(fbid=link_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    link_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Link(fbid=link_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    link_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Link(fbid=link_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_comment(
    link_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Link(fbid=link_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_likes(
    link_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Link(fbid=link_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


# Export the server
link_server = mcp
