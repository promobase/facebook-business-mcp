"""
Auto-generated MCP server for Facebook Tab.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.tab import Tab
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-tab")


# CRUD Operations


@mcp.tool()
async def api_create_tab(
    tab_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Tab(fbid=tab_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_tab(
    tab_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Tab(fbid=tab_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_tab(
    tab_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Tab(fbid=tab_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_tab(
    tab_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Tab(fbid=tab_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
tab_server = mcp
