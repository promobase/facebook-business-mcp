"""
Auto-generated MCP server for Facebook Status.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.status import Status
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-status")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    status_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Status(fbid=status_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    status_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Status(fbid=status_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    status_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Status(fbid=status_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    status_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Status(fbid=status_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def create_like(
    status_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Status(fbid=status_id).create_like(
        fields=fields,
        params=params,
    )

    return result


# Export the server
status_server = mcp
