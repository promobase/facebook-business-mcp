"""
Auto-generated MCP server for Facebook ALMEndAdvertiserInfo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.almendadvertiserinfo import ALMEndAdvertiserInfo
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-almendadvertiserinfo")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    almendadvertiserinfo_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ALMEndAdvertiserInfo(fbid=almendadvertiserinfo_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    almendadvertiserinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ALMEndAdvertiserInfo(fbid=almendadvertiserinfo_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    almendadvertiserinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ALMEndAdvertiserInfo(fbid=almendadvertiserinfo_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    almendadvertiserinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ALMEndAdvertiserInfo(fbid=almendadvertiserinfo_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
almendadvertiserinfo_server = mcp
