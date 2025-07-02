"""
Auto-generated MCP server for Facebook EventSourceGroup.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.eventsourcegroup import EventSourceGroup
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-eventsourcegroup")


# CRUD Operations


@mcp.tool()
async def create_eventsourcegroup(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventSourceGroup(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_eventsourcegroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventSourceGroup(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_eventsourcegroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventSourceGroup(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_eventsourcegroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventSourceGroup(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_shared_account_for_eventsourcegroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventSourceGroup(fbid=object_id).create_shared_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shared_accounts_for_eventsourcegroup(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = EventSourceGroup(fbid=object_id).get_shared_accounts(
        fields=fields,
        params=params,
    )

    return result


# Export the server
eventsourcegroup_server = mcp
