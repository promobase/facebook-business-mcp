"""
Auto-generated MCP server for Facebook CatalogWebsiteSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.catalogwebsitesettings import CatalogWebsiteSettings
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-catalogwebsitesettings")


# CRUD Operations


@mcp.tool()
async def api_create_catalogwebsitesettings(
    catalogwebsitesettings_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CatalogWebsiteSettings(fbid=catalogwebsitesettings_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_catalogwebsitesettings(
    catalogwebsitesettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CatalogWebsiteSettings(fbid=catalogwebsitesettings_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_catalogwebsitesettings(
    catalogwebsitesettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CatalogWebsiteSettings(fbid=catalogwebsitesettings_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_catalogwebsitesettings(
    catalogwebsitesettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CatalogWebsiteSettings(fbid=catalogwebsitesettings_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
catalogwebsitesettings_server = mcp
