"""
Auto-generated MCP server for Facebook Hours.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.hours import Hours
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-hours")


# CRUD Operations


@mcp.tool()
async def get_hours(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Hours.

    Args:
        object_id: The ID of the Hours
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Hours(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
hours_server = mcp
