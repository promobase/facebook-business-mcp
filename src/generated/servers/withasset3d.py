"""
Auto-generated MCP server for Facebook WithAsset3D.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.withasset3d import WithAsset3D
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-withasset3d")


# CRUD Operations


@mcp.tool()
async def get_withasset3d(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a WithAsset3D.

    Args:
        object_id: The ID of the WithAsset3D
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = WithAsset3D(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
withasset3d_server = mcp
