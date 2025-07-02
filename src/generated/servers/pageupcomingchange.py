"""
Auto-generated MCP server for Facebook PageUpcomingChange.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pageupcomingchange import PageUpcomingChange
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-pageupcomingchange")


# CRUD Operations


@mcp.tool()
async def api_create_pageupcomingchange(
    pageupcomingchange_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageUpcomingChange(fbid=pageupcomingchange_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_pageupcomingchange(
    pageupcomingchange_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageUpcomingChange(fbid=pageupcomingchange_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_pageupcomingchange(
    pageupcomingchange_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageUpcomingChange(fbid=pageupcomingchange_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_pageupcomingchange(
    pageupcomingchange_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = PageUpcomingChange(fbid=pageupcomingchange_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pageupcomingchange_server = mcp
