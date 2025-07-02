"""
Auto-generated MCP server for Facebook CanvasTemplate.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.canvastemplate import CanvasTemplate
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-canvastemplate")


# CRUD Operations


@mcp.tool()
async def api_create_canvastemplate(
    canvastemplate_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CanvasTemplate(fbid=canvastemplate_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_canvastemplate(
    canvastemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CanvasTemplate(fbid=canvastemplate_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_canvastemplate(
    canvastemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CanvasTemplate(fbid=canvastemplate_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_canvastemplate(
    canvastemplate_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CanvasTemplate(fbid=canvastemplate_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
canvastemplate_server = mcp
