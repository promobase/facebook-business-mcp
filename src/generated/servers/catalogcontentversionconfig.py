"""
Auto-generated MCP server for Facebook CatalogContentVersionConfig.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.catalogcontentversionconfig import CatalogContentVersionConfig
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-catalogcontentversionconfig")


# CRUD Operations


@mcp.tool()
async def api_create_catalogcontentversionconfig(
    catalogcontentversionconfig_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CatalogContentVersionConfig(fbid=catalogcontentversionconfig_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_catalogcontentversionconfig(
    catalogcontentversionconfig_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CatalogContentVersionConfig(fbid=catalogcontentversionconfig_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_catalogcontentversionconfig(
    catalogcontentversionconfig_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CatalogContentVersionConfig(fbid=catalogcontentversionconfig_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_catalogcontentversionconfig(
    catalogcontentversionconfig_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = CatalogContentVersionConfig(fbid=catalogcontentversionconfig_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
catalogcontentversionconfig_server = mcp
