"""
Auto-generated MCP server for Facebook FavoriteCatalog.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.favoritecatalog import FavoriteCatalog
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-favoritecatalog")


# CRUD Operations


@mcp.tool()
async def api_create_favoritecatalog(
    favoritecatalog_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FavoriteCatalog(fbid=favoritecatalog_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_favoritecatalog(
    favoritecatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FavoriteCatalog(fbid=favoritecatalog_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_favoritecatalog(
    favoritecatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FavoriteCatalog(fbid=favoritecatalog_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_favoritecatalog(
    favoritecatalog_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = FavoriteCatalog(fbid=favoritecatalog_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
favoritecatalog_server = mcp
