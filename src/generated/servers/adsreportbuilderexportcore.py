"""
Auto-generated MCP server for Facebook AdsReportBuilderExportCore.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adsreportbuilderexportcore import AdsReportBuilderExportCore
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adsreportbuilderexportcore")


# CRUD Operations


@mcp.tool()
async def get_adsreportbuilderexportcore(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdsReportBuilderExportCore.

    Args:
        object_id: The ID of the AdsReportBuilderExportCore
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdsReportBuilderExportCore(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adsreportbuilderexportcore_server = mcp
