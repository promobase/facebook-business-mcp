"""
Auto-generated MCP server for Facebook AdSavedLocation.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsavedlocation import AdSavedLocation
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsavedlocation")


# CRUD Operations


@mcp.tool()
async def api_create_adsavedlocation(
    adsavedlocation_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdSavedLocation(fbid=adsavedlocation_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adsavedlocation(
    adsavedlocation_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdSavedLocation(fbid=adsavedlocation_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adsavedlocation(
    adsavedlocation_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdSavedLocation(fbid=adsavedlocation_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adsavedlocation(
    adsavedlocation_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdSavedLocation(fbid=adsavedlocation_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsavedlocation_server = mcp
