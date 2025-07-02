"""
Auto-generated MCP server for Facebook CPASParentCatalogSettings.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.cpasparentcatalogsettings import CPASParentCatalogSettings
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-cpasparentcatalogsettings")


# CRUD Operations


@mcp.tool()
async def get_cpasparentcatalogsettings(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CPASParentCatalogSettings.

    Args:
        object_id: The ID of the CPASParentCatalogSettings
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CPASParentCatalogSettings(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
cpasparentcatalogsettings_server = mcp
