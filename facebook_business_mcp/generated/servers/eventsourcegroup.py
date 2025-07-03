"""
Auto-generated MCP server for Facebook EventSourceGroup.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.eventsourcegroup import EventSourceGroup
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-eventsourcegroup")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    eventsourcegroup_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = EventSourceGroup(fbid=eventsourcegroup_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    eventsourcegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = EventSourceGroup(fbid=eventsourcegroup_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    eventsourcegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = EventSourceGroup(fbid=eventsourcegroup_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    eventsourcegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = EventSourceGroup(fbid=eventsourcegroup_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_shared_account(
    eventsourcegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = EventSourceGroup(fbid=eventsourcegroup_id).create_shared_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_shared_accounts(
    eventsourcegroup_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = EventSourceGroup(fbid=eventsourcegroup_id).get_shared_accounts(
        fields=fields,
        params=params,
    )

    return result


# Export the server
eventsourcegroup_server = mcp
