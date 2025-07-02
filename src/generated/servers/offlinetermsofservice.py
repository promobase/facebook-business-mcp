"""
Auto-generated MCP server for Facebook OfflineTermsOfService.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.offlinetermsofservice import OfflineTermsOfService
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-offlinetermsofservice")


# CRUD Operations


@mcp.tool()
async def api_create_offlinetermsofservice(
    offlinetermsofservice_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineTermsOfService(fbid=offlinetermsofservice_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_offlinetermsofservice(
    offlinetermsofservice_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineTermsOfService(fbid=offlinetermsofservice_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_offlinetermsofservice(
    offlinetermsofservice_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineTermsOfService(fbid=offlinetermsofservice_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_offlinetermsofservice(
    offlinetermsofservice_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = OfflineTermsOfService(fbid=offlinetermsofservice_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
offlinetermsofservice_server = mcp
