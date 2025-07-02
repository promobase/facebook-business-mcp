"""
Auto-generated MCP server for Facebook ManagementSiteLink.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.managementsitelink import ManagementSiteLink
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-managementsitelink")


# CRUD Operations


@mcp.tool()
async def api_create_managementsitelink(
    managementsitelink_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ManagementSiteLink(fbid=managementsitelink_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_managementsitelink(
    managementsitelink_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ManagementSiteLink(fbid=managementsitelink_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_managementsitelink(
    managementsitelink_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ManagementSiteLink(fbid=managementsitelink_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_managementsitelink(
    managementsitelink_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ManagementSiteLink(fbid=managementsitelink_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
managementsitelink_server = mcp
