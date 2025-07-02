"""
Auto-generated MCP server for Facebook ImageReferenceMatch.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.imagereferencematch import ImageReferenceMatch
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-imagereferencematch")


# CRUD Operations


@mcp.tool()
async def get_imagereferencematch(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ImageReferenceMatch.

    Args:
        object_id: The ID of the ImageReferenceMatch
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ImageReferenceMatch(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
imagereferencematch_server = mcp
