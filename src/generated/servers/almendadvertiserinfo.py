"""
Auto-generated MCP server for Facebook ALMEndAdvertiserInfo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.almendadvertiserinfo import ALMEndAdvertiserInfo
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-almendadvertiserinfo")


# CRUD Operations


@mcp.tool()
async def api_create_almendadvertiserinfo(
    almendadvertiserinfo_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ALMEndAdvertiserInfo(fbid=almendadvertiserinfo_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_almendadvertiserinfo(
    almendadvertiserinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ALMEndAdvertiserInfo(fbid=almendadvertiserinfo_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_almendadvertiserinfo(
    almendadvertiserinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ALMEndAdvertiserInfo(fbid=almendadvertiserinfo_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_almendadvertiserinfo(
    almendadvertiserinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ALMEndAdvertiserInfo(fbid=almendadvertiserinfo_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
almendadvertiserinfo_server = mcp
