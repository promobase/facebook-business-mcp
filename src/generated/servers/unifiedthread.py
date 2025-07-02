"""
Auto-generated MCP server for Facebook UnifiedThread.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.unifiedthread import UnifiedThread
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-unifiedthread")


# CRUD Operations


@mcp.tool()
async def get_unifiedthread(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a UnifiedThread.

    Args:
        object_id: The ID of the UnifiedThread
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = UnifiedThread(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_messages_for_unifiedthread(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Messages for UnifiedThread.

    Args:
        object_id: The ID of the UnifiedThread
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_messages result
    """
    result = UnifiedThread(fbid=object_id).get_messages(
        fields=fields,
        params=params,
    )

    return result


# Export the server
unifiedthread_server = mcp
