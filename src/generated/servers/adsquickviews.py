"""
Auto-generated MCP server for Facebook AdsQuickViews.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsquickviews import AdsQuickViews
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsquickviews")


# CRUD Operations


@mcp.tool()
async def api_create_adsquickviews(
    adsquickviews_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsQuickViews(fbid=adsquickviews_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adsquickviews(
    adsquickviews_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsQuickViews(fbid=adsquickviews_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adsquickviews(
    adsquickviews_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsQuickViews(fbid=adsquickviews_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adsquickviews(
    adsquickviews_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdsQuickViews(fbid=adsquickviews_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsquickviews_server = mcp
