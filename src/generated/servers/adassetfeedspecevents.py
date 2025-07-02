"""
Auto-generated MCP server for Facebook AdAssetFeedSpecEvents.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adassetfeedspecevents import AdAssetFeedSpecEvents
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adassetfeedspecevents")


# CRUD Operations


@mcp.tool()
async def api_create_adassetfeedspecevents(
    adassetfeedspecevents_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetFeedSpecEvents(fbid=adassetfeedspecevents_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adassetfeedspecevents(
    adassetfeedspecevents_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetFeedSpecEvents(fbid=adassetfeedspecevents_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adassetfeedspecevents(
    adassetfeedspecevents_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetFeedSpecEvents(fbid=adassetfeedspecevents_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adassetfeedspecevents(
    adassetfeedspecevents_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAssetFeedSpecEvents(fbid=adassetfeedspecevents_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adassetfeedspecevents_server = mcp
