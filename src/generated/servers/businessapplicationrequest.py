"""
Auto-generated MCP server for Facebook BusinessApplicationRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessapplicationrequest import BusinessApplicationRequest
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessapplicationrequest")


# CRUD Operations


@mcp.tool()
async def api_create_businessapplicationrequest(
    businessapplicationrequest_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessApplicationRequest(fbid=businessapplicationrequest_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_businessapplicationrequest(
    businessapplicationrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessApplicationRequest(fbid=businessapplicationrequest_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_businessapplicationrequest(
    businessapplicationrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessApplicationRequest(fbid=businessapplicationrequest_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_businessapplicationrequest(
    businessapplicationrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BusinessApplicationRequest(fbid=businessapplicationrequest_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessapplicationrequest_server = mcp
