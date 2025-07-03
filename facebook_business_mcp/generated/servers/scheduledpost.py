"""
Auto-generated MCP server for Facebook ScheduledPost.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.scheduledpost import ScheduledPost
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-scheduledpost")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    scheduledpost_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ScheduledPost(fbid=scheduledpost_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    scheduledpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ScheduledPost(fbid=scheduledpost_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    scheduledpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ScheduledPost(fbid=scheduledpost_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    scheduledpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ScheduledPost(fbid=scheduledpost_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
scheduledpost_server = mcp
