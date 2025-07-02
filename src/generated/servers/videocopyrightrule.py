"""
Auto-generated MCP server for Facebook VideoCopyrightRule.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.videocopyrightrule import VideoCopyrightRule
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-videocopyrightrule")


# CRUD Operations


@mcp.tool()
async def get_videocopyrightrule(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a VideoCopyrightRule.

    Args:
        object_id: The ID of the VideoCopyrightRule
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = VideoCopyrightRule(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
videocopyrightrule_server = mcp
