"""
Auto-generated MCP server for Facebook AdAsyncRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adasyncrequest import AdAsyncRequest
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adasyncrequest")


# CRUD Operations


@mcp.tool()
async def api_create_adasyncrequest(
    adasyncrequest_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAsyncRequest(fbid=adasyncrequest_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adasyncrequest(
    adasyncrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAsyncRequest(fbid=adasyncrequest_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adasyncrequest(
    adasyncrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAsyncRequest(fbid=adasyncrequest_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adasyncrequest(
    adasyncrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAsyncRequest(fbid=adasyncrequest_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adasyncrequest_server = mcp
