"""
Auto-generated MCP server for Facebook AppRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.apprequest import AppRequest
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-apprequest")


# CRUD Operations


@mcp.tool()
async def delete_apprequest(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a AppRequest.

    Args:
        object_id: The ID of the AppRequest
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = AppRequest(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_apprequest(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AppRequest.

    Args:
        object_id: The ID of the AppRequest
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AppRequest(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
apprequest_server = mcp
