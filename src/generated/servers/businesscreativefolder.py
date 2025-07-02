"""
Auto-generated MCP server for Facebook BusinessCreativeFolder.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businesscreativefolder import BusinessCreativeFolder
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-businesscreativefolder")


# CRUD Operations


@mcp.tool()
async def create_businesscreativefolder(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a BusinessCreativeFolder.

    Args:
        object_id: The ID of the BusinessCreativeFolder
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = BusinessCreativeFolder(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_businesscreativefolder(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a BusinessCreativeFolder.

    Args:
        object_id: The ID of the BusinessCreativeFolder
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = BusinessCreativeFolder(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businesscreativefolder_server = mcp
