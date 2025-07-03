"""
Auto-generated MCP server for Facebook ManagementSiteLink.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.managementsitelink import ManagementSiteLink
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-managementsitelink")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    managementsitelink_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ManagementSiteLink(fbid=managementsitelink_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    managementsitelink_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ManagementSiteLink(fbid=managementsitelink_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    managementsitelink_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ManagementSiteLink(fbid=managementsitelink_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    managementsitelink_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ManagementSiteLink(fbid=managementsitelink_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
managementsitelink_server = mcp
