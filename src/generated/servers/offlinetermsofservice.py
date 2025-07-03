"""
Auto-generated MCP server for Facebook OfflineTermsOfService.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.offlinetermsofservice import OfflineTermsOfService
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-offlinetermsofservice")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    offlinetermsofservice_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineTermsOfService(fbid=offlinetermsofservice_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    offlinetermsofservice_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineTermsOfService(fbid=offlinetermsofservice_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    offlinetermsofservice_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineTermsOfService(fbid=offlinetermsofservice_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    offlinetermsofservice_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = OfflineTermsOfService(fbid=offlinetermsofservice_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
offlinetermsofservice_server = mcp
