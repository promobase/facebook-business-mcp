"""
Auto-generated MCP server for Facebook ProductFeedSchedule.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productfeedschedule import ProductFeedSchedule
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productfeedschedule")


# CRUD Operations


@mcp.tool()
async def get_productfeedschedule(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ProductFeedSchedule.

    Args:
        object_id: The ID of the ProductFeedSchedule
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ProductFeedSchedule(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productfeedschedule_server = mcp
