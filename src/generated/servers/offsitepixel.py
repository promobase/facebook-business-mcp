"""
Auto-generated MCP server for Facebook OffsitePixel.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.offsitepixel import OffsitePixel
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-offsitepixel")


# CRUD Operations


@mcp.tool()
async def get_offsitepixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a OffsitePixel.

    Args:
        object_id: The ID of the OffsitePixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = OffsitePixel(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
offsitepixel_server = mcp
