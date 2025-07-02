"""
Auto-generated MCP server for Facebook UserIDForPage.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.useridforpage import UserIDForPage
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-useridforpage")


# CRUD Operations


@mcp.tool()
async def create_useridforpage(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UserIDForPage(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_useridforpage(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UserIDForPage(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_useridforpage(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UserIDForPage(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_useridforpage(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UserIDForPage(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
useridforpage_server = mcp
