"""
Auto-generated MCP server for Facebook BusinessPageRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businesspagerequest import BusinessPageRequest
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businesspagerequest")


# CRUD Operations


@mcp.tool()
async def api_create_businesspagerequest(
    businesspagerequest_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessPageRequest(fbid=businesspagerequest_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_businesspagerequest(
    businesspagerequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessPageRequest(fbid=businesspagerequest_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_businesspagerequest(
    businesspagerequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessPageRequest(fbid=businesspagerequest_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_businesspagerequest(
    businesspagerequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessPageRequest(fbid=businesspagerequest_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businesspagerequest_server = mcp
