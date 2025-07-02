"""
Auto-generated MCP server for Facebook BusinessCreativeFolder.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businesscreativefolder import BusinessCreativeFolder
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businesscreativefolder")


# CRUD Operations


@mcp.tool()
async def api_create_businesscreativefolder(
    businesscreativefolder_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessCreativeFolder(fbid=businesscreativefolder_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_businesscreativefolder(
    businesscreativefolder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessCreativeFolder(fbid=businesscreativefolder_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_businesscreativefolder(
    businesscreativefolder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessCreativeFolder(fbid=businesscreativefolder_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_businesscreativefolder(
    businesscreativefolder_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessCreativeFolder(fbid=businesscreativefolder_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businesscreativefolder_server = mcp
