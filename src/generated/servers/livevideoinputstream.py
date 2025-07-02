"""
Auto-generated MCP server for Facebook LiveVideoInputStream.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.livevideoinputstream import LiveVideoInputStream
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-livevideoinputstream")


# CRUD Operations


@mcp.tool()
async def get_livevideoinputstream(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a LiveVideoInputStream.

    Args:
        object_id: The ID of the LiveVideoInputStream
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = LiveVideoInputStream(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
livevideoinputstream_server = mcp
