"""
Auto-generated MCP server for Facebook BusinessRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessrequest import BusinessRequest
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessrequest")


# CRUD Operations


@mcp.tool()
async def api_create_businessrequest(
    businessrequest_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessRequest(fbid=businessrequest_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_businessrequest(
    businessrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessRequest(fbid=businessrequest_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_businessrequest(
    businessrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessRequest(fbid=businessrequest_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_businessrequest(
    businessrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessRequest(fbid=businessrequest_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessrequest_server = mcp
