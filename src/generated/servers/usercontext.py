"""
Auto-generated MCP server for Facebook UserContext.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.usercontext import UserContext
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-usercontext")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    usercontext_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = UserContext(fbid=usercontext_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    usercontext_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = UserContext(fbid=usercontext_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    usercontext_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = UserContext(fbid=usercontext_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    usercontext_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = UserContext(fbid=usercontext_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
usercontext_server = mcp
