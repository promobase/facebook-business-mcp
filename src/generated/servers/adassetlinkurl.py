"""
Auto-generated MCP server for Facebook AdAssetLinkURL.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adassetlinkurl import AdAssetLinkURL
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adassetlinkurl")


# CRUD Operations


@mcp.tool()
async def api_create_adassetlinkurl(
    adassetlinkurl_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetLinkURL(fbid=adassetlinkurl_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adassetlinkurl(
    adassetlinkurl_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetLinkURL(fbid=adassetlinkurl_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adassetlinkurl(
    adassetlinkurl_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetLinkURL(fbid=adassetlinkurl_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adassetlinkurl(
    adassetlinkurl_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetLinkURL(fbid=adassetlinkurl_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adassetlinkurl_server = mcp
