"""
Auto-generated MCP server for Facebook BusinessImageTBusinessFolderPathItem.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessimagetbusinessfolderpathitem import (
    BusinessImageTBusinessFolderPathItem,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessimagetbusinessfolderpathitem")


# CRUD Operations


@mcp.tool()
async def api_create_businessimagetbusinessfolderpathitem(
    businessimagetbusinessfolderpathitem_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessImageTBusinessFolderPathItem(
        fbid=businessimagetbusinessfolderpathitem_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_businessimagetbusinessfolderpathitem(
    businessimagetbusinessfolderpathitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessImageTBusinessFolderPathItem(
        fbid=businessimagetbusinessfolderpathitem_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_businessimagetbusinessfolderpathitem(
    businessimagetbusinessfolderpathitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessImageTBusinessFolderPathItem(
        fbid=businessimagetbusinessfolderpathitem_id
    ).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_businessimagetbusinessfolderpathitem(
    businessimagetbusinessfolderpathitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessImageTBusinessFolderPathItem(
        fbid=businessimagetbusinessfolderpathitem_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessimagetbusinessfolderpathitem_server = mcp
