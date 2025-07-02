"""
Auto-generated MCP server for Facebook PagePublisher.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pagepublisher import PagePublisher
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-pagepublisher")


# CRUD Operations


@mcp.tool()
async def api_create_pagepublisher(
    pagepublisher_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePublisher(fbid=pagepublisher_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_pagepublisher(
    pagepublisher_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePublisher(fbid=pagepublisher_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_pagepublisher(
    pagepublisher_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePublisher(fbid=pagepublisher_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_pagepublisher(
    pagepublisher_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PagePublisher(fbid=pagepublisher_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pagepublisher_server = mcp
