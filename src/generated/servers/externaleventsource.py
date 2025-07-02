"""
Auto-generated MCP server for Facebook ExternalEventSource.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.externaleventsource import ExternalEventSource
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-externaleventsource")


# CRUD Operations


@mcp.tool()
async def api_create_externaleventsource(
    externaleventsource_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExternalEventSource(fbid=externaleventsource_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_externaleventsource(
    externaleventsource_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExternalEventSource(fbid=externaleventsource_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_externaleventsource(
    externaleventsource_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExternalEventSource(fbid=externaleventsource_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_externaleventsource(
    externaleventsource_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ExternalEventSource(fbid=externaleventsource_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
externaleventsource_server = mcp
