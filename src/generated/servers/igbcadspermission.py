"""
Auto-generated MCP server for Facebook IGBCAdsPermission.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igbcadspermission import IGBCAdsPermission
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-igbcadspermission")


# CRUD Operations


@mcp.tool()
async def api_create_igbcadspermission(
    igbcadspermission_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGBCAdsPermission(fbid=igbcadspermission_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_igbcadspermission(
    igbcadspermission_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGBCAdsPermission(fbid=igbcadspermission_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_igbcadspermission(
    igbcadspermission_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGBCAdsPermission(fbid=igbcadspermission_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_igbcadspermission(
    igbcadspermission_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGBCAdsPermission(fbid=igbcadspermission_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igbcadspermission_server = mcp
