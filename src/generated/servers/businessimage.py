"""
Auto-generated MCP server for Facebook BusinessImage.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessimage import BusinessImage
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businessimage")


# CRUD Operations


@mcp.tool()
async def create_businessimage(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a BusinessImage.

    Args:
        object_id: The ID of the BusinessImage
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = BusinessImage(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_businessimage(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BusinessImage.

    Args:
        object_id: The ID of the BusinessImage
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BusinessImage(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessimage_server = mcp
