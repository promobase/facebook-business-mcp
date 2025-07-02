"""
Auto-generated MCP server for Facebook ManagedPartnerBusiness.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.managedpartnerbusiness import ManagedPartnerBusiness
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-managedpartnerbusiness")


# CRUD Operations


@mcp.tool()
async def create_managedpartnerbusiness(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a ManagedPartnerBusiness.

    Args:
        object_id: The ID of the ManagedPartnerBusiness
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = ManagedPartnerBusiness(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


# Export the server
managedpartnerbusiness_server = mcp
