"""
Auto-generated MCP server for Facebook IGBCAdsPermission.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igbcadspermission import IGBCAdsPermission
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-igbcadspermission")


# CRUD Operations


@mcp.tool()
async def get_igbcadspermission(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a IGBCAdsPermission.

    Args:
        object_id: The ID of the IGBCAdsPermission
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = IGBCAdsPermission(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igbcadspermission_server = mcp
