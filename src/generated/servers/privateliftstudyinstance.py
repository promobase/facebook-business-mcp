"""
Auto-generated MCP server for Facebook PrivateLiftStudyInstance.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.privateliftstudyinstance import PrivateLiftStudyInstance
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-privateliftstudyinstance")


# CRUD Operations


@mcp.tool()
async def get_privateliftstudyinstance(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a PrivateLiftStudyInstance.

    Args:
        object_id: The ID of the PrivateLiftStudyInstance
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = PrivateLiftStudyInstance(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_privateliftstudyinstance(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a PrivateLiftStudyInstance.

    Args:
        object_id: The ID of the PrivateLiftStudyInstance
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = PrivateLiftStudyInstance(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
privateliftstudyinstance_server = mcp
