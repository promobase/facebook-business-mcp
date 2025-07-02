"""
Auto-generated MCP server for Facebook Organization.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.organization import Organization
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-organization")


# CRUD Operations


@mcp.tool()
async def get_organization(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Organization.

    Args:
        object_id: The ID of the Organization
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Organization(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
organization_server = mcp
