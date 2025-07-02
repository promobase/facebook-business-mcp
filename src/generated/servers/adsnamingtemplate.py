"""
Auto-generated MCP server for Facebook AdsNamingTemplate.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsnamingtemplate import AdsNamingTemplate
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsnamingtemplate")


# CRUD Operations


@mcp.tool()
async def get_adsnamingtemplate(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdsNamingTemplate.

    Args:
        object_id: The ID of the AdsNamingTemplate
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdsNamingTemplate(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsnamingtemplate_server = mcp
