"""
Auto-generated MCP server for Facebook ALMEvent.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.almevent import ALMEvent
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-almevent")


# CRUD Operations


@mcp.tool()
async def api_create_almevent(
    almevent_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ALMEvent(fbid=almevent_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_almevent(
    almevent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ALMEvent(fbid=almevent_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_almevent(
    almevent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ALMEvent(fbid=almevent_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_almevent(
    almevent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ALMEvent(fbid=almevent_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
almevent_server = mcp
