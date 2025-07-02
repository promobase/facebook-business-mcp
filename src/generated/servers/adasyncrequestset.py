"""
Auto-generated MCP server for Facebook AdAsyncRequestSet.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adasyncrequestset import AdAsyncRequestSet
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adasyncrequestset")


# CRUD Operations


@mcp.tool()
async def api_create_adasyncrequestset(
    adasyncrequestset_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAsyncRequestSet(fbid=adasyncrequestset_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adasyncrequestset(
    adasyncrequestset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAsyncRequestSet(fbid=adasyncrequestset_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adasyncrequestset(
    adasyncrequestset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAsyncRequestSet(fbid=adasyncrequestset_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adasyncrequestset(
    adasyncrequestset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAsyncRequestSet(fbid=adasyncrequestset_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_requests(
    adasyncrequestset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAsyncRequestSet(fbid=adasyncrequestset_id).get_requests(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adasyncrequestset_server = mcp
