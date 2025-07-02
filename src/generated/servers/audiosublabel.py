"""
Auto-generated MCP server for Facebook AudioSubLabel.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.audiosublabel import AudioSubLabel
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-audiosublabel")


# CRUD Operations


@mcp.tool()
async def get_audiosublabel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AudioSubLabel.

    Args:
        object_id: The ID of the AudioSubLabel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AudioSubLabel(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
audiosublabel_server = mcp
