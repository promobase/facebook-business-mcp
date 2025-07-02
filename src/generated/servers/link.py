"""
Auto-generated MCP server for Facebook Link.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.link import Link
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-link")


# CRUD Operations


@mcp.tool()
async def api_create_link(
    link_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Link(fbid=link_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_link(
    link_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Link(fbid=link_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_link(
    link_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Link(fbid=link_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_link(
    link_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Link(fbid=link_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_comment(
    link_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Link(fbid=link_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_likes(
    link_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Link(fbid=link_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


# Export the server
link_server = mcp
