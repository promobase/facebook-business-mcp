"""
Auto-generated MCP server for Facebook IGRefreshAccessTokenForIGOnlyAPI.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igrefreshaccesstokenforigonlyapi import (
    IGRefreshAccessTokenForIGOnlyAPI,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-igrefreshaccesstokenforigonlyapi")


# CRUD Operations


@mcp.tool()
async def api_create_igrefreshaccesstokenforigonlyapi(
    igrefreshaccesstokenforigonlyapi_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGRefreshAccessTokenForIGOnlyAPI(fbid=igrefreshaccesstokenforigonlyapi_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_igrefreshaccesstokenforigonlyapi(
    igrefreshaccesstokenforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGRefreshAccessTokenForIGOnlyAPI(fbid=igrefreshaccesstokenforigonlyapi_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_igrefreshaccesstokenforigonlyapi(
    igrefreshaccesstokenforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGRefreshAccessTokenForIGOnlyAPI(fbid=igrefreshaccesstokenforigonlyapi_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_igrefreshaccesstokenforigonlyapi(
    igrefreshaccesstokenforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGRefreshAccessTokenForIGOnlyAPI(fbid=igrefreshaccesstokenforigonlyapi_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igrefreshaccesstokenforigonlyapi_server = mcp
