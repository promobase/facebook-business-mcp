"""
Auto-generated MCP server for Facebook BusinessOwnedObjectOnBehalfOfRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessownedobjectonbehalfofrequest import (
    BusinessOwnedObjectOnBehalfOfRequest,
)
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-businessownedobjectonbehalfofrequest")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    businessownedobjectonbehalfofrequest_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessOwnedObjectOnBehalfOfRequest(
        fbid=businessownedobjectonbehalfofrequest_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    businessownedobjectonbehalfofrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessOwnedObjectOnBehalfOfRequest(
        fbid=businessownedobjectonbehalfofrequest_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    businessownedobjectonbehalfofrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessOwnedObjectOnBehalfOfRequest(
        fbid=businessownedobjectonbehalfofrequest_id
    ).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    businessownedobjectonbehalfofrequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessOwnedObjectOnBehalfOfRequest(
        fbid=businessownedobjectonbehalfofrequest_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessownedobjectonbehalfofrequest_server = mcp
