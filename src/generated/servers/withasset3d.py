"""
Auto-generated MCP server for Facebook WithAsset3D.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.withasset3d import WithAsset3D
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-withasset3d")


# CRUD Operations


@mcp.tool()
async def create_withasset3d(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WithAsset3D(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_withasset3d(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WithAsset3D(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_withasset3d(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WithAsset3D(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_withasset3d(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = WithAsset3D(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
withasset3d_server = mcp
