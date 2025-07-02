"""
Auto-generated MCP server for Facebook EventExternalTicketInfo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.eventexternalticketinfo import EventExternalTicketInfo
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-eventexternalticketinfo")


# CRUD Operations


@mcp.tool()
async def api_create_eventexternalticketinfo(
    eventexternalticketinfo_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventExternalTicketInfo(fbid=eventexternalticketinfo_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_eventexternalticketinfo(
    eventexternalticketinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventExternalTicketInfo(fbid=eventexternalticketinfo_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_eventexternalticketinfo(
    eventexternalticketinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventExternalTicketInfo(fbid=eventexternalticketinfo_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_eventexternalticketinfo(
    eventexternalticketinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventExternalTicketInfo(fbid=eventexternalticketinfo_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
eventexternalticketinfo_server = mcp
