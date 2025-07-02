"""
Auto-generated MCP server for Facebook AdCustomDerivedMetrics.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adcustomderivedmetrics import AdCustomDerivedMetrics
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adcustomderivedmetrics")


# CRUD Operations


@mcp.tool()
async def get_adcustomderivedmetrics(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdCustomDerivedMetrics.

    Args:
        object_id: The ID of the AdCustomDerivedMetrics
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdCustomDerivedMetrics(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adcustomderivedmetrics_server = mcp
