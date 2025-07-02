"""
Auto-generated MCP server for Facebook SavedAudience.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.savedaudience import SavedAudience
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-savedaudience")


# CRUD Operations


@mcp.tool()
async def get_savedaudience(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a SavedAudience.

    Args:
        object_id: The ID of the SavedAudience
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = SavedAudience(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
savedaudience_server = mcp
