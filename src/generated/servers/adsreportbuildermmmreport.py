"""
Auto-generated MCP server for Facebook AdsReportBuilderMMMReport.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsreportbuildermmmreport import AdsReportBuilderMMMReport
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsreportbuildermmmreport")


# CRUD Operations


@mcp.tool()
async def get_adsreportbuildermmmreport(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdsReportBuilderMMMReport.

    Args:
        object_id: The ID of the AdsReportBuilderMMMReport
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdsReportBuilderMMMReport(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsreportbuildermmmreport_server = mcp
