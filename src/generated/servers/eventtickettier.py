"""
Auto-generated MCP server for Facebook EventTicketTier.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.eventtickettier import EventTicketTier
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-eventtickettier")


# CRUD Operations


@mcp.tool()
async def api_create_eventtickettier(
    eventtickettier_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventTicketTier(fbid=eventtickettier_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_eventtickettier(
    eventtickettier_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventTicketTier(fbid=eventtickettier_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_eventtickettier(
    eventtickettier_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventTicketTier(fbid=eventtickettier_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_eventtickettier(
    eventtickettier_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventTicketTier(fbid=eventtickettier_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
eventtickettier_server = mcp
