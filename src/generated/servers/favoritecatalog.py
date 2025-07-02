"""
Auto-generated MCP server for Facebook FavoriteCatalog.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.favoritecatalog import FavoriteCatalog
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-favoritecatalog")


# CRUD Operations


@mcp.tool()
async def get_favoritecatalog(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a FavoriteCatalog.

    Args:
        object_id: The ID of the FavoriteCatalog
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = FavoriteCatalog(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
favoritecatalog_server = mcp
