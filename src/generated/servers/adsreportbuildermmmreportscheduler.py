"""
Auto-generated MCP server for Facebook AdsReportBuilderMMMReportScheduler.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsreportbuildermmmreportscheduler import (
    AdsReportBuilderMMMReportScheduler,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsreportbuildermmmreportscheduler")


# CRUD Operations


@mcp.tool()
async def get_adsreportbuildermmmreportscheduler(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdsReportBuilderMMMReportScheduler.

    Args:
        object_id: The ID of the AdsReportBuilderMMMReportScheduler
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdsReportBuilderMMMReportScheduler(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsreportbuildermmmreportscheduler_server = mcp
