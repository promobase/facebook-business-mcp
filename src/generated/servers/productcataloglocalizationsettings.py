"""
Auto-generated MCP server for Facebook ProductCatalogLocalizationSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productcataloglocalizationsettings import (
    ProductCatalogLocalizationSettings,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productcataloglocalizationsettings")


# CRUD Operations


@mcp.tool()
async def api_create_productcataloglocalizationsettings(
    productcataloglocalizationsettings_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductCatalogLocalizationSettings(
        fbid=productcataloglocalizationsettings_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_productcataloglocalizationsettings(
    productcataloglocalizationsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductCatalogLocalizationSettings(
        fbid=productcataloglocalizationsettings_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_productcataloglocalizationsettings(
    productcataloglocalizationsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductCatalogLocalizationSettings(fbid=productcataloglocalizationsettings_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_productcataloglocalizationsettings(
    productcataloglocalizationsettings_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductCatalogLocalizationSettings(
        fbid=productcataloglocalizationsettings_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productcataloglocalizationsettings_server = mcp
