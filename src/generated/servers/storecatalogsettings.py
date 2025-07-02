"""
Auto-generated MCP server for Facebook StoreCatalogSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.storecatalogsettings import StoreCatalogSettings
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-storecatalogsettings")


# CRUD Operations


@mcp.tool()
async def create_storecatalogsettings(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a StoreCatalogSettings.

    Args:
        object_id: The ID of the StoreCatalogSettings
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = StoreCatalogSettings(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_storecatalogsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a StoreCatalogSettings.

    Args:
        object_id: The ID of the StoreCatalogSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = StoreCatalogSettings(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_storecatalogsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a StoreCatalogSettings.

    Args:
        object_id: The ID of the StoreCatalogSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = StoreCatalogSettings(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
storecatalogsettings_server = mcp
