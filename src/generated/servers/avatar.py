"""
Auto-generated MCP server for Facebook Avatar.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.avatar import Avatar
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-avatar")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    avatar_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Avatar(fbid=avatar_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    avatar_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Avatar(fbid=avatar_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    avatar_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Avatar(fbid=avatar_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    avatar_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Avatar(fbid=avatar_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_models(
    avatar_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = Avatar(fbid=avatar_id).get_models(
        fields=fields,
        params=params,
    )

    return result


# Export the server
avatar_server = mcp
