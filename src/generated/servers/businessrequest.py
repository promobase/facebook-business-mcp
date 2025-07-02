"""
Auto-generated MCP server for Facebook BusinessRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessrequest import BusinessRequest
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessrequest")


# CRUD Operations


@mcp.tool()
async def get_businessrequest(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BusinessRequest.

    Args:
        object_id: The ID of the BusinessRequest
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BusinessRequest(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessrequest_server = mcp
