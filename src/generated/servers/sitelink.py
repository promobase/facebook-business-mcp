"""
Auto-generated MCP server for Facebook SiteLink.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.sitelink import SiteLink
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-sitelink")


# CRUD Operations


@mcp.tool()
async def api_create_sitelink(
    sitelink_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SiteLink(fbid=sitelink_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_sitelink(
    sitelink_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SiteLink(fbid=sitelink_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_sitelink(
    sitelink_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SiteLink(fbid=sitelink_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_sitelink(
    sitelink_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SiteLink(fbid=sitelink_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
sitelink_server = mcp
