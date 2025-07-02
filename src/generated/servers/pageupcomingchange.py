"""
Auto-generated MCP server for Facebook PageUpcomingChange.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pageupcomingchange import PageUpcomingChange
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-pageupcomingchange")


# CRUD Operations


@mcp.tool()
async def get_pageupcomingchange(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a PageUpcomingChange.

    Args:
        object_id: The ID of the PageUpcomingChange
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = PageUpcomingChange(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pageupcomingchange_server = mcp
