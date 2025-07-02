"""
Auto-generated MCP server for Facebook FantasyGame.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.fantasygame import FantasyGame
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-fantasygame")


# CRUD Operations


@mcp.tool()
async def get_fantasygame(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a FantasyGame.

    Args:
        object_id: The ID of the FantasyGame
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = FantasyGame(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
fantasygame_server = mcp
