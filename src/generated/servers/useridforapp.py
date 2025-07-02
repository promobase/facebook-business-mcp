"""
Auto-generated MCP server for Facebook UserIDForApp.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.useridforapp import UserIDForApp
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-useridforapp")


# CRUD Operations


@mcp.tool()
async def api_create_useridforapp(
    useridforapp_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UserIDForApp(fbid=useridforapp_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_useridforapp(
    useridforapp_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UserIDForApp(fbid=useridforapp_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_useridforapp(
    useridforapp_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UserIDForApp(fbid=useridforapp_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_useridforapp(
    useridforapp_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = UserIDForApp(fbid=useridforapp_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
useridforapp_server = mcp
