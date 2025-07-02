"""
Auto-generated MCP server for Facebook CanvasDynamicSetting.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.canvasdynamicsetting import CanvasDynamicSetting
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-canvasdynamicsetting")


# CRUD Operations


@mcp.tool()
async def api_create_canvasdynamicsetting(
    canvasdynamicsetting_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CanvasDynamicSetting(fbid=canvasdynamicsetting_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_canvasdynamicsetting(
    canvasdynamicsetting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CanvasDynamicSetting(fbid=canvasdynamicsetting_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_canvasdynamicsetting(
    canvasdynamicsetting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CanvasDynamicSetting(fbid=canvasdynamicsetting_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_canvasdynamicsetting(
    canvasdynamicsetting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CanvasDynamicSetting(fbid=canvasdynamicsetting_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
canvasdynamicsetting_server = mcp
