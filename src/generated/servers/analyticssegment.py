"""
Auto-generated MCP server for Facebook AnalyticsSegment.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.analyticssegment import AnalyticsSegment
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-analyticssegment")


# CRUD Operations


@mcp.tool()
async def get_analyticssegment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AnalyticsSegment.

    Args:
        object_id: The ID of the AnalyticsSegment
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AnalyticsSegment(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
analyticssegment_server = mcp
