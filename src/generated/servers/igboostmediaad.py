"""
Auto-generated MCP server for Facebook IGBoostMediaAd.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igboostmediaad import IGBoostMediaAd
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-igboostmediaad")


# CRUD Operations


@mcp.tool()
async def api_create_igboostmediaad(
    igboostmediaad_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGBoostMediaAd(fbid=igboostmediaad_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_igboostmediaad(
    igboostmediaad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGBoostMediaAd(fbid=igboostmediaad_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_igboostmediaad(
    igboostmediaad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGBoostMediaAd(fbid=igboostmediaad_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_igboostmediaad(
    igboostmediaad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = IGBoostMediaAd(fbid=igboostmediaad_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igboostmediaad_server = mcp
