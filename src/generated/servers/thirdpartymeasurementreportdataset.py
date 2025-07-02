"""
Auto-generated MCP server for Facebook ThirdPartyMeasurementReportDataset.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.thirdpartymeasurementreportdataset import (
    ThirdPartyMeasurementReportDataset,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-thirdpartymeasurementreportdataset")


# CRUD Operations


@mcp.tool()
async def get_thirdpartymeasurementreportdataset(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ThirdPartyMeasurementReportDataset.

    Args:
        object_id: The ID of the ThirdPartyMeasurementReportDataset
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ThirdPartyMeasurementReportDataset(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
thirdpartymeasurementreportdataset_server = mcp
