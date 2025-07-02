"""
Auto-generated MCP server for Facebook CopyrightMediaMisuse.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.copyrightmediamisuse import CopyrightMediaMisuse
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-copyrightmediamisuse")


# CRUD Operations


@mcp.tool()
async def get_copyrightmediamisuse(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CopyrightMediaMisuse.

    Args:
        object_id: The ID of the CopyrightMediaMisuse
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CopyrightMediaMisuse(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
copyrightmediamisuse_server = mcp
