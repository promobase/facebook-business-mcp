"""
Auto-generated MCP server for Facebook MeasurementReport.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.measurementreport import MeasurementReport
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-measurementreport")


# CRUD Operations


@mcp.tool()
async def get_measurementreport(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a MeasurementReport.

    Args:
        object_id: The ID of the MeasurementReport
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = MeasurementReport(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
measurementreport_server = mcp
