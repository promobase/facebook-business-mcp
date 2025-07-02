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
async def create_canvastemplate(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CanvasTemplate(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_canvastemplate(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CanvasTemplate(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_canvastemplate(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CanvasTemplate(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_canvastemplate(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CanvasTemplate(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
canvastemplate_server = mcp
