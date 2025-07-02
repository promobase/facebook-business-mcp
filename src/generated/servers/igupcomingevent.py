"""
Auto-generated MCP server for Facebook IGUpcomingEvent.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igupcomingevent import IGUpcomingEvent
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-igupcomingevent")


# CRUD Operations


@mcp.tool()
async def api_create_igupcomingevent(
    igupcomingevent_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUpcomingEvent(fbid=igupcomingevent_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_igupcomingevent(
    igupcomingevent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUpcomingEvent(fbid=igupcomingevent_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_igupcomingevent(
    igupcomingevent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUpcomingEvent(fbid=igupcomingevent_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_igupcomingevent(
    igupcomingevent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGUpcomingEvent(fbid=igupcomingevent_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igupcomingevent_server = mcp
