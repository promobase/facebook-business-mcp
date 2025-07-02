"""
Auto-generated MCP server for Facebook SocialWifiSite.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.socialwifisite import SocialWifiSite
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-socialwifisite")


# CRUD Operations


@mcp.tool()
async def api_create_socialwifisite(
    socialwifisite_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SocialWifiSite(fbid=socialwifisite_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_socialwifisite(
    socialwifisite_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SocialWifiSite(fbid=socialwifisite_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_socialwifisite(
    socialwifisite_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SocialWifiSite(fbid=socialwifisite_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_socialwifisite(
    socialwifisite_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = SocialWifiSite(fbid=socialwifisite_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
socialwifisite_server = mcp
