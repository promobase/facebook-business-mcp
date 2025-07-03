"""
Auto-generated MCP server for Facebook ExternalEventSource.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.externaleventsource import ExternalEventSource
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-externaleventsource")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    externaleventsource_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExternalEventSource(fbid=externaleventsource_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    externaleventsource_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExternalEventSource(fbid=externaleventsource_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    externaleventsource_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExternalEventSource(fbid=externaleventsource_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    externaleventsource_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ExternalEventSource(fbid=externaleventsource_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
externaleventsource_server = mcp
