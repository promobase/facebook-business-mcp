"""
Auto-generated MCP server for Facebook AdgroupFacebookFeedback.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adgroupfacebookfeedback import AdgroupFacebookFeedback
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adgroupfacebookfeedback")


# Edge Methods


@mcp.tool()
async def get_comments_for_adgroupfacebookfeedback(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Comments for AdgroupFacebookFeedback.

    Args:
        object_id: The ID of the AdgroupFacebookFeedback
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_comments result
    """
    result = AdgroupFacebookFeedback(fbid=object_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adgroupfacebookfeedback_server = mcp
