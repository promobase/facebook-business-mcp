"""
Auto-generated MCP server for Facebook StoreLocation.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.storelocation import StoreLocation
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-storelocation")


# CRUD Operations


@mcp.tool()
async def get_storelocation(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a StoreLocation.

    Args:
        object_id: The ID of the StoreLocation
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = StoreLocation(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
storelocation_server = mcp
