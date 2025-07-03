"""
Auto-generated MCP server for Facebook WhitehatFBDLRun.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.whitehatfbdlrun import WhitehatFBDLRun
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-whitehatfbdlrun")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    whitehatfbdlrun_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WhitehatFBDLRun(fbid=whitehatfbdlrun_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    whitehatfbdlrun_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WhitehatFBDLRun(fbid=whitehatfbdlrun_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    whitehatfbdlrun_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WhitehatFBDLRun(fbid=whitehatfbdlrun_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    whitehatfbdlrun_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = WhitehatFBDLRun(fbid=whitehatfbdlrun_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
whitehatfbdlrun_server = mcp
