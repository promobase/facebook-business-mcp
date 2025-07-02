"""
Auto-generated MCP server for Facebook LifeEvent.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.lifeevent import LifeEvent
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-lifeevent")


# CRUD Operations


@mcp.tool()
async def api_create_lifeevent(
    lifeevent_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LifeEvent(fbid=lifeevent_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_lifeevent(
    lifeevent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LifeEvent(fbid=lifeevent_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_lifeevent(
    lifeevent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LifeEvent(fbid=lifeevent_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_lifeevent(
    lifeevent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LifeEvent(fbid=lifeevent_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_likes(
    lifeevent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LifeEvent(fbid=lifeevent_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


# Export the server
lifeevent_server = mcp
