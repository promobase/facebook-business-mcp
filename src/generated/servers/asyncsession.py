"""
Auto-generated MCP server for Facebook AsyncSession.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.asyncsession import AsyncSession
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-asyncsession")


# CRUD Operations


@mcp.tool()
async def get_asyncsession(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AsyncSession.

    Args:
        object_id: The ID of the AsyncSession
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AsyncSession(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
asyncsession_server = mcp
