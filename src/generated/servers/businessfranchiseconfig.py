"""
Auto-generated MCP server for Facebook BusinessFranchiseConfig.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessfranchiseconfig import BusinessFranchiseConfig
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessfranchiseconfig")


# CRUD Operations


@mcp.tool()
async def get_businessfranchiseconfig(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BusinessFranchiseConfig.

    Args:
        object_id: The ID of the BusinessFranchiseConfig
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BusinessFranchiseConfig(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessfranchiseconfig_server = mcp
