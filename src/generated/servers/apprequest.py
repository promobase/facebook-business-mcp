"""
Auto-generated MCP server for Facebook AppRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.apprequest import AppRequest
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-apprequest")


# CRUD Operations


@mcp.tool()
async def api_create_apprequest(
    apprequest_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AppRequest(fbid=apprequest_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_apprequest(
    apprequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AppRequest(fbid=apprequest_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_apprequest(
    apprequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AppRequest(fbid=apprequest_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_apprequest(
    apprequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AppRequest(fbid=apprequest_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
apprequest_server = mcp
