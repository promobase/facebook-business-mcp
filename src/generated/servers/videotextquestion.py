"""
Auto-generated MCP server for Facebook VideoTextQuestion.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.videotextquestion import VideoTextQuestion
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-videotextquestion")


# CRUD Operations


@mcp.tool()
async def get_videotextquestion(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a VideoTextQuestion.

    Args:
        object_id: The ID of the VideoTextQuestion
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = VideoTextQuestion(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
videotextquestion_server = mcp
