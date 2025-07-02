"""
Auto-generated MCP server for Facebook AdSavedReport.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsavedreport import AdSavedReport
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsavedreport")


# CRUD Operations


@mcp.tool()
async def get_adsavedreport(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdSavedReport.

    Args:
        object_id: The ID of the AdSavedReport
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdSavedReport(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsavedreport_server = mcp
