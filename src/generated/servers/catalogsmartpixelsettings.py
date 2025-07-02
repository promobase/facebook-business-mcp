"""
Auto-generated MCP server for Facebook CatalogSmartPixelSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.catalogsmartpixelsettings import CatalogSmartPixelSettings
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-catalogsmartpixelsettings")


# CRUD Operations


@mcp.tool()
async def api_create_catalogsmartpixelsettings(
    catalogsmartpixelsettings_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CatalogSmartPixelSettings(fbid=catalogsmartpixelsettings_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_catalogsmartpixelsettings(
    catalogsmartpixelsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CatalogSmartPixelSettings(fbid=catalogsmartpixelsettings_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_catalogsmartpixelsettings(
    catalogsmartpixelsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CatalogSmartPixelSettings(fbid=catalogsmartpixelsettings_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_catalogsmartpixelsettings(
    catalogsmartpixelsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CatalogSmartPixelSettings(fbid=catalogsmartpixelsettings_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
catalogsmartpixelsettings_server = mcp
