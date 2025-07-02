"""
Auto-generated MCP server for Facebook AdsPivotRules.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adspivotrules import AdsPivotRules
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adspivotrules")


# CRUD Operations


@mcp.tool()
async def get_adspivotrules(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdsPivotRules.

    Args:
        object_id: The ID of the AdsPivotRules
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdsPivotRules(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adspivotrules_server = mcp
