"""
Auto-generated MCP server for Facebook RTBDynamicPost.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.rtbdynamicpost import RTBDynamicPost
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-rtbdynamicpost")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    rtbdynamicpost_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = RTBDynamicPost(fbid=rtbdynamicpost_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    rtbdynamicpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = RTBDynamicPost(fbid=rtbdynamicpost_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    rtbdynamicpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = RTBDynamicPost(fbid=rtbdynamicpost_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    rtbdynamicpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = RTBDynamicPost(fbid=rtbdynamicpost_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_comments(
    rtbdynamicpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = RTBDynamicPost(fbid=rtbdynamicpost_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def get_likes(
    rtbdynamicpost_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = RTBDynamicPost(fbid=rtbdynamicpost_id).get_likes(
        fields=fields,
        params=params,
    )

    return result


# Export the server
rtbdynamicpost_server = mcp
