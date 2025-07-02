"""
Auto-generated MCP server for Facebook EventTicketSetting.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.eventticketsetting import EventTicketSetting
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-eventticketsetting")


# CRUD Operations


@mcp.tool()
async def api_create_eventticketsetting(
    eventticketsetting_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventTicketSetting(fbid=eventticketsetting_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_eventticketsetting(
    eventticketsetting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventTicketSetting(fbid=eventticketsetting_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_eventticketsetting(
    eventticketsetting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventTicketSetting(fbid=eventticketsetting_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_eventticketsetting(
    eventticketsetting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventTicketSetting(fbid=eventticketsetting_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
eventticketsetting_server = mcp
