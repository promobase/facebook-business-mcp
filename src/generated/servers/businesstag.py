"""
Auto-generated MCP server for Facebook BusinessTag.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businesstag import BusinessTag
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businesstag")


# CRUD Operations


@mcp.tool()
async def api_create_businesstag(
    businesstag_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessTag(fbid=businesstag_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_businesstag(
    businesstag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessTag(fbid=businesstag_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_businesstag(
    businesstag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessTag(fbid=businesstag_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_businesstag(
    businesstag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessTag(fbid=businesstag_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businesstag_server = mcp
