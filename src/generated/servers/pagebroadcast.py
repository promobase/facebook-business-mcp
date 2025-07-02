"""
Auto-generated MCP server for Facebook PageBroadcast.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pagebroadcast import PageBroadcast
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-pagebroadcast")


# CRUD Operations


@mcp.tool()
async def api_create_pagebroadcast(
    pagebroadcast_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageBroadcast(fbid=pagebroadcast_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_pagebroadcast(
    pagebroadcast_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageBroadcast(fbid=pagebroadcast_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_pagebroadcast(
    pagebroadcast_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageBroadcast(fbid=pagebroadcast_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_pagebroadcast(
    pagebroadcast_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageBroadcast(fbid=pagebroadcast_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pagebroadcast_server = mcp
