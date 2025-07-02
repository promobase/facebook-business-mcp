"""
Auto-generated MCP server for Facebook IGAccessTokenForIGOnlyAPI.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igaccesstokenforigonlyapi import IGAccessTokenForIGOnlyAPI
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-igaccesstokenforigonlyapi")


# CRUD Operations


@mcp.tool()
async def api_create_igaccesstokenforigonlyapi(
    igaccesstokenforigonlyapi_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGAccessTokenForIGOnlyAPI(fbid=igaccesstokenforigonlyapi_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_igaccesstokenforigonlyapi(
    igaccesstokenforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGAccessTokenForIGOnlyAPI(fbid=igaccesstokenforigonlyapi_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_igaccesstokenforigonlyapi(
    igaccesstokenforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGAccessTokenForIGOnlyAPI(fbid=igaccesstokenforigonlyapi_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_igaccesstokenforigonlyapi(
    igaccesstokenforigonlyapi_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGAccessTokenForIGOnlyAPI(fbid=igaccesstokenforigonlyapi_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igaccesstokenforigonlyapi_server = mcp
