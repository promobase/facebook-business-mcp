"""
Auto-generated MCP server for Facebook AdAsyncRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adasyncrequest import AdAsyncRequest
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adasyncrequest")


# CRUD Operations


@mcp.tool()
async def delete_adasyncrequest(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a AdAsyncRequest.

    Args:
        object_id: The ID of the AdAsyncRequest
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = AdAsyncRequest(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adasyncrequest(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdAsyncRequest.

    Args:
        object_id: The ID of the AdAsyncRequest
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdAsyncRequest(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adasyncrequest_server = mcp
