"""
Auto-generated MCP server for Facebook ImageCopyrightDispute.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.imagecopyrightdispute import ImageCopyrightDispute
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-imagecopyrightdispute")


# CRUD Operations


@mcp.tool()
async def get_imagecopyrightdispute(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ImageCopyrightDispute.

    Args:
        object_id: The ID of the ImageCopyrightDispute
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ImageCopyrightDispute(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
imagecopyrightdispute_server = mcp
