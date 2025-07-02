"""
Auto-generated MCP server for Facebook InstagramThread.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.instagramthread import InstagramThread
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-instagramthread")


# CRUD Operations


@mcp.tool()
async def api_create_instagramthread(
    instagramthread_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = InstagramThread(fbid=instagramthread_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_instagramthread(
    instagramthread_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = InstagramThread(fbid=instagramthread_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_instagramthread(
    instagramthread_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = InstagramThread(fbid=instagramthread_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_instagramthread(
    instagramthread_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = InstagramThread(fbid=instagramthread_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
instagramthread_server = mcp
