"""
Auto-generated MCP server for Facebook AudioIsrc.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.audioisrc import AudioIsrc
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-audioisrc")


# CRUD Operations


@mcp.tool()
async def get_audioisrc(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AudioIsrc.

    Args:
        object_id: The ID of the AudioIsrc
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AudioIsrc(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
audioisrc_server = mcp
