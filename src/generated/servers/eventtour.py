"""
Auto-generated MCP server for Facebook EventTour.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.eventtour import EventTour
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-eventtour")


# CRUD Operations


@mcp.tool()
async def api_create_eventtour(
    eventtour_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventTour(fbid=eventtour_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_eventtour(
    eventtour_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventTour(fbid=eventtour_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_eventtour(
    eventtour_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventTour(fbid=eventtour_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_eventtour(
    eventtour_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventTour(fbid=eventtour_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
eventtour_server = mcp
