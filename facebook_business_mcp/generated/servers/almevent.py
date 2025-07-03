"""
Auto-generated MCP server for Facebook ALMEvent.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.almevent import ALMEvent
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-almevent")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    almevent_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ALMEvent(fbid=almevent_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    almevent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ALMEvent(fbid=almevent_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    almevent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ALMEvent(fbid=almevent_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    almevent_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ALMEvent(fbid=almevent_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
almevent_server = mcp
