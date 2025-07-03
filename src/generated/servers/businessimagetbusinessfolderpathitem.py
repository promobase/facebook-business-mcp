"""
Auto-generated MCP server for Facebook BusinessImageTBusinessFolderPathItem.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessimagetbusinessfolderpathitem import (
    BusinessImageTBusinessFolderPathItem,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-businessimagetbusinessfolderpathitem")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    businessimagetbusinessfolderpathitem_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessImageTBusinessFolderPathItem(
        fbid=businessimagetbusinessfolderpathitem_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    businessimagetbusinessfolderpathitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessImageTBusinessFolderPathItem(
        fbid=businessimagetbusinessfolderpathitem_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    businessimagetbusinessfolderpathitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessImageTBusinessFolderPathItem(
        fbid=businessimagetbusinessfolderpathitem_id
    ).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    businessimagetbusinessfolderpathitem_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessImageTBusinessFolderPathItem(
        fbid=businessimagetbusinessfolderpathitem_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessimagetbusinessfolderpathitem_server = mcp
