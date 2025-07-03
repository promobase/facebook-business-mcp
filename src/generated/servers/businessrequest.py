"""
Auto-generated MCP server for Facebook BusinessRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessrequest import BusinessRequest
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-businessrequest")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    businessrequest_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessRequest(fbid=businessrequest_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    businessrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessRequest(fbid=businessrequest_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    businessrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessRequest(fbid=businessrequest_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    businessrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessRequest(fbid=businessrequest_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessrequest_server = mcp
