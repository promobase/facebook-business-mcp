"""
Auto-generated MCP server for Facebook BusinessVideoTBusinessFolderPathItem.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessvideotbusinessfolderpathitem import (
    BusinessVideoTBusinessFolderPathItem,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessvideotbusinessfolderpathitem")


# CRUD Operations


@mcp.tool()
async def api_create_businessvideotbusinessfolderpathitem(
    businessvideotbusinessfolderpathitem_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessVideoTBusinessFolderPathItem(
        fbid=businessvideotbusinessfolderpathitem_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_businessvideotbusinessfolderpathitem(
    businessvideotbusinessfolderpathitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessVideoTBusinessFolderPathItem(
        fbid=businessvideotbusinessfolderpathitem_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_businessvideotbusinessfolderpathitem(
    businessvideotbusinessfolderpathitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessVideoTBusinessFolderPathItem(
        fbid=businessvideotbusinessfolderpathitem_id
    ).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_businessvideotbusinessfolderpathitem(
    businessvideotbusinessfolderpathitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessVideoTBusinessFolderPathItem(
        fbid=businessvideotbusinessfolderpathitem_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessvideotbusinessfolderpathitem_server = mcp
