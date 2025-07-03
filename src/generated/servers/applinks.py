"""
Auto-generated MCP server for Facebook AppLinks.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.applinks import AppLinks
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-applinks")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    applinks_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AppLinks(fbid=applinks_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    applinks_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AppLinks(fbid=applinks_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    applinks_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AppLinks(fbid=applinks_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    applinks_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AppLinks(fbid=applinks_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
applinks_server = mcp
