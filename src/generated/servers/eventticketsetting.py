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
async def create_eventticketsetting(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventTicketSetting(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_eventticketsetting(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventTicketSetting(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_eventticketsetting(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventTicketSetting(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_eventticketsetting(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventTicketSetting(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
eventticketsetting_server = mcp
