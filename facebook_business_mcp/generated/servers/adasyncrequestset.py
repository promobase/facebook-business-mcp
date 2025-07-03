"""
Auto-generated MCP server for Facebook AdAsyncRequestSet.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adasyncrequestset import AdAsyncRequestSet
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-adasyncrequestset")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    adasyncrequestset_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAsyncRequestSet(fbid=adasyncrequestset_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    adasyncrequestset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAsyncRequestSet(fbid=adasyncrequestset_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    adasyncrequestset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAsyncRequestSet(fbid=adasyncrequestset_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    adasyncrequestset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAsyncRequestSet(fbid=adasyncrequestset_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
@wrapped_fn_tool
async def get_requests(
    adasyncrequestset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdAsyncRequestSet(fbid=adasyncrequestset_id).get_requests(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adasyncrequestset_server = mcp
