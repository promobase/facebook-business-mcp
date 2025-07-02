"""
Auto-generated MCP server for Facebook Status.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.status import Status
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-status")


# CRUD Operations


@mcp.tool()
async def get_status(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Status.

    Args:
        object_id: The ID of the Status
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Status(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_like_for_status(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Like for Status.

    Args:
        object_id: The ID of the Status
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_like result
    """
    result = Status(fbid=object_id).create_like(
        fields=fields,
        params=params,
    )

    return result


# Export the server
status_server = mcp
