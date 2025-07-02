"""
Auto-generated MCP server for Facebook PageCategory.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pagecategory import PageCategory
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-pagecategory")


# CRUD Operations


@mcp.tool()
async def api_create_pagecategory(
    pagecategory_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageCategory(fbid=pagecategory_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_pagecategory(
    pagecategory_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageCategory(fbid=pagecategory_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_pagecategory(
    pagecategory_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageCategory(fbid=pagecategory_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_pagecategory(
    pagecategory_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageCategory(fbid=pagecategory_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pagecategory_server = mcp
