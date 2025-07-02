"""
Auto-generated MCP server for Facebook CatalogWebsiteOnboardingSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.catalogwebsiteonboardingsettings import (
    CatalogWebsiteOnboardingSettings,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-catalogwebsiteonboardingsettings")


# CRUD Operations


@mcp.tool()
async def api_create_catalogwebsiteonboardingsettings(
    catalogwebsiteonboardingsettings_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CatalogWebsiteOnboardingSettings(fbid=catalogwebsiteonboardingsettings_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_catalogwebsiteonboardingsettings(
    catalogwebsiteonboardingsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CatalogWebsiteOnboardingSettings(fbid=catalogwebsiteonboardingsettings_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_catalogwebsiteonboardingsettings(
    catalogwebsiteonboardingsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CatalogWebsiteOnboardingSettings(fbid=catalogwebsiteonboardingsettings_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_catalogwebsiteonboardingsettings(
    catalogwebsiteonboardingsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CatalogWebsiteOnboardingSettings(fbid=catalogwebsiteonboardingsettings_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
catalogwebsiteonboardingsettings_server = mcp
