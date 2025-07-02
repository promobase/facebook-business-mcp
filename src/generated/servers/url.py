"""
Auto-generated MCP server for Facebook URL.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.url import URL
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-url")


# CRUD Operations


@mcp.tool()
async def api_create_url(
    url_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = URL(fbid=url_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_url(
    url_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = URL(fbid=url_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_url(
    url_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = URL(fbid=url_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_url(
    url_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = URL(fbid=url_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
url_server = mcp
