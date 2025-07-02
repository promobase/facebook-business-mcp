"""
Auto-generated MCP server for Facebook BidSchedule.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.bidschedule import BidSchedule
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-bidschedule")


# CRUD Operations


@mcp.tool()
async def create_bidschedule(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BidSchedule(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_bidschedule(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BidSchedule(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_bidschedule(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BidSchedule(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_bidschedule(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BidSchedule(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
bidschedule_server = mcp
