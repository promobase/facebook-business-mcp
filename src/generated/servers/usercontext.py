"""
Auto-generated MCP server for Facebook UserContext.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.usercontext import UserContext
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-usercontext")


# CRUD Operations


@mcp.tool()
async def get_usercontext(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a UserContext.

    Args:
        object_id: The ID of the UserContext
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = UserContext(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
usercontext_server = mcp
