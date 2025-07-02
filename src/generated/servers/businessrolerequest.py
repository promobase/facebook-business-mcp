"""
Auto-generated MCP server for Facebook BusinessRoleRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessrolerequest import BusinessRoleRequest
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessrolerequest")


# CRUD Operations


@mcp.tool()
async def delete_businessrolerequest(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a BusinessRoleRequest.

    Args:
        object_id: The ID of the BusinessRoleRequest
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = BusinessRoleRequest(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_businessrolerequest(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BusinessRoleRequest.

    Args:
        object_id: The ID of the BusinessRoleRequest
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BusinessRoleRequest(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_businessrolerequest(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a BusinessRoleRequest.

    Args:
        object_id: The ID of the BusinessRoleRequest
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = BusinessRoleRequest(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessrolerequest_server = mcp
