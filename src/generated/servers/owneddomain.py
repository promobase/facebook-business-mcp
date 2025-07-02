"""
Auto-generated MCP server for Facebook OwnedDomain.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.owneddomain import OwnedDomain
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-owneddomain")


# CRUD Operations


@mcp.tool()
async def get_owneddomain(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a OwnedDomain.

    Args:
        object_id: The ID of the OwnedDomain
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = OwnedDomain(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
owneddomain_server = mcp
