"""
Auto-generated MCP server for Facebook CloudGame.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.cloudgame import CloudGame
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-cloudgame")


# CRUD Operations


@mcp.tool()
async def get_cloudgame(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a CloudGame.

    Args:
        object_id: The ID of the CloudGame
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = CloudGame(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
cloudgame_server = mcp
