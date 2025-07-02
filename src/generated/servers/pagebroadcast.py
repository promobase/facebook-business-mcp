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
async def create_pagebroadcast(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageBroadcast(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_pagebroadcast(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageBroadcast(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pagebroadcast(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageBroadcast(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_pagebroadcast(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageBroadcast(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pagebroadcast_server = mcp
