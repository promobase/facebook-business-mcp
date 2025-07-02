"""
Auto-generated MCP server for Facebook LoomConfig.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.loomconfig import LoomConfig
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-loomconfig")


# CRUD Operations


@mcp.tool()
async def api_create_loomconfig(
    loomconfig_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LoomConfig(fbid=loomconfig_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_loomconfig(
    loomconfig_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LoomConfig(fbid=loomconfig_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_loomconfig(
    loomconfig_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LoomConfig(fbid=loomconfig_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_loomconfig(
    loomconfig_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = LoomConfig(fbid=loomconfig_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
loomconfig_server = mcp
