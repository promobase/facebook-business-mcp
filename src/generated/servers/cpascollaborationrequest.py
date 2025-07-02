"""
Auto-generated MCP server for Facebook CPASCollaborationRequest.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.cpascollaborationrequest import CPASCollaborationRequest
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-cpascollaborationrequest")


# CRUD Operations


@mcp.tool()
async def create_cpascollaborationrequest(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a CPASCollaborationRequest.

    Args:
        object_id: The ID of the CPASCollaborationRequest
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = CPASCollaborationRequest(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_cpascollaborationrequest(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CPASCollaborationRequest.

    Args:
        object_id: The ID of the CPASCollaborationRequest
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CPASCollaborationRequest(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
cpascollaborationrequest_server = mcp
