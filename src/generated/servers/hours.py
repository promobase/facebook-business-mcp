"""
Auto-generated MCP server for Facebook Hours.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.hours import Hours
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-hours")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    hours_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Hours(fbid=hours_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    hours_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Hours(fbid=hours_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    hours_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Hours(fbid=hours_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    hours_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Hours(fbid=hours_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
hours_server = mcp
