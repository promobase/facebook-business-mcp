"""
Auto-generated MCP server for Facebook IGBCAdsPermission.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igbcadspermission import IGBCAdsPermission
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-igbcadspermission")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    igbcadspermission_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGBCAdsPermission(fbid=igbcadspermission_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    igbcadspermission_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGBCAdsPermission(fbid=igbcadspermission_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    igbcadspermission_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGBCAdsPermission(fbid=igbcadspermission_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    igbcadspermission_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = IGBCAdsPermission(fbid=igbcadspermission_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igbcadspermission_server = mcp
