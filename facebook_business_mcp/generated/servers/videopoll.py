"""
Auto-generated MCP server for Facebook VideoPoll.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.videopoll import VideoPoll
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-videopoll")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    videopoll_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoPoll(fbid=videopoll_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    videopoll_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoPoll(fbid=videopoll_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    videopoll_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoPoll(fbid=videopoll_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    videopoll_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoPoll(fbid=videopoll_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_poll_options(
    videopoll_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = VideoPoll(fbid=videopoll_id).get_poll_options(
        fields=fields,
        params=params,
    )

    return result


# Export the server
videopoll_server = mcp
