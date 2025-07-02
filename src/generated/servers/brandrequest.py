"""
Auto-generated MCP server for Facebook BrandRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.brandrequest import BrandRequest
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-brandrequest")


# CRUD Operations


@mcp.tool()
async def get_brandrequest(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BrandRequest.

    Args:
        object_id: The ID of the BrandRequest
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BrandRequest(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
brandrequest_server = mcp
