"""
Auto-generated MCP server for Facebook AsyncRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.asyncrequest import AsyncRequest
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-asyncrequest")


# CRUD Operations


@mcp.tool()
async def api_create_asyncrequest(
    asyncrequest_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AsyncRequest(fbid=asyncrequest_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_asyncrequest(
    asyncrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AsyncRequest(fbid=asyncrequest_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_asyncrequest(
    asyncrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AsyncRequest(fbid=asyncrequest_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_asyncrequest(
    asyncrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AsyncRequest(fbid=asyncrequest_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
asyncrequest_server = mcp
