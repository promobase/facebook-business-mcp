"""
Auto-generated MCP server for Facebook ConnectionsTargeting.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.connectionstargeting import ConnectionsTargeting
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-connectionstargeting")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    connectionstargeting_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ConnectionsTargeting(fbid=connectionstargeting_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    connectionstargeting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ConnectionsTargeting(fbid=connectionstargeting_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    connectionstargeting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ConnectionsTargeting(fbid=connectionstargeting_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    connectionstargeting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ConnectionsTargeting(fbid=connectionstargeting_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
connectionstargeting_server = mcp
