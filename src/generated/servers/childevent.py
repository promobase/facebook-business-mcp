"""
Auto-generated MCP server for Facebook ChildEvent.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.childevent import ChildEvent
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-childevent")


# CRUD Operations


@mcp.tool()
async def api_create_childevent(
    childevent_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ChildEvent(fbid=childevent_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_childevent(
    childevent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ChildEvent(fbid=childevent_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_childevent(
    childevent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ChildEvent(fbid=childevent_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_childevent(
    childevent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ChildEvent(fbid=childevent_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
childevent_server = mcp
