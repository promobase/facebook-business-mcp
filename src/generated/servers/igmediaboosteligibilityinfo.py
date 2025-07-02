"""
Auto-generated MCP server for Facebook IGMediaBoostEligibilityInfo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igmediaboosteligibilityinfo import IGMediaBoostEligibilityInfo
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-igmediaboosteligibilityinfo")


# CRUD Operations


@mcp.tool()
async def get_igmediaboosteligibilityinfo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a IGMediaBoostEligibilityInfo.

    Args:
        object_id: The ID of the IGMediaBoostEligibilityInfo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = IGMediaBoostEligibilityInfo(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igmediaboosteligibilityinfo_server = mcp
