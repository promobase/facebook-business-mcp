"""
Auto-generated MCP server for Facebook AnalyticsUserConfig.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.analyticsuserconfig import AnalyticsUserConfig
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-analyticsuserconfig")


# CRUD Operations


@mcp.tool()
async def get_analyticsuserconfig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AnalyticsUserConfig.

    Args:
        object_id: The ID of the AnalyticsUserConfig
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AnalyticsUserConfig(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
analyticsuserconfig_server = mcp
