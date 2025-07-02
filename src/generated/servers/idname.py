"""
Auto-generated MCP server for Facebook IDName.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.idname import IDName
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-idname")


# CRUD Operations


@mcp.tool()
async def api_create_idname(
    idname_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IDName(fbid=idname_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_idname(
    idname_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IDName(fbid=idname_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_idname(
    idname_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IDName(fbid=idname_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_idname(
    idname_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IDName(fbid=idname_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
idname_server = mcp
