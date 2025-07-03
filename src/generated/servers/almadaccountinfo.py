"""
Auto-generated MCP server for Facebook ALMAdAccountInfo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.almadaccountinfo import ALMAdAccountInfo
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-almadaccountinfo")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    almadaccountinfo_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ALMAdAccountInfo(fbid=almadaccountinfo_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    almadaccountinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ALMAdAccountInfo(fbid=almadaccountinfo_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    almadaccountinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ALMAdAccountInfo(fbid=almadaccountinfo_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    almadaccountinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ALMAdAccountInfo(fbid=almadaccountinfo_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
almadaccountinfo_server = mcp
