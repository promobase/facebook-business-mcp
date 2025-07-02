"""
Auto-generated MCP server for Facebook AdsReportBuilderSavedReport.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsreportbuildersavedreport import AdsReportBuilderSavedReport
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsreportbuildersavedreport")


# CRUD Operations


@mcp.tool()
async def get_adsreportbuildersavedreport(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdsReportBuilderSavedReport.

    Args:
        object_id: The ID of the AdsReportBuilderSavedReport
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdsReportBuilderSavedReport(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsreportbuildersavedreport_server = mcp
