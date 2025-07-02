"""
Auto-generated MCP server for Facebook UnifiedThread.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.unifiedthread import UnifiedThread
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-unifiedthread")


# CRUD Operations


@mcp.tool()
async def api_create_unifiedthread(
    unifiedthread_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UnifiedThread(fbid=unifiedthread_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_unifiedthread(
    unifiedthread_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UnifiedThread(fbid=unifiedthread_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_unifiedthread(
    unifiedthread_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UnifiedThread(fbid=unifiedthread_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_unifiedthread(
    unifiedthread_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UnifiedThread(fbid=unifiedthread_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_messages(
    unifiedthread_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UnifiedThread(fbid=unifiedthread_id).get_messages(
        fields=fields,
        params=params,
    )

    return result


# Export the server
unifiedthread_server = mcp
