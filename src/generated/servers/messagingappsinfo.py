"""
Auto-generated MCP server for Facebook MessagingAppsInfo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.messagingappsinfo import MessagingAppsInfo
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-messagingappsinfo")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    messagingappsinfo_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MessagingAppsInfo(fbid=messagingappsinfo_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    messagingappsinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MessagingAppsInfo(fbid=messagingappsinfo_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    messagingappsinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MessagingAppsInfo(fbid=messagingappsinfo_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    messagingappsinfo_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = MessagingAppsInfo(fbid=messagingappsinfo_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
messagingappsinfo_server = mcp
