"""
Auto-generated MCP server for Facebook Stories.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.stories import Stories
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-stories")


# CRUD Operations


@mcp.tool()
async def get_stories(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a Stories.

    Args:
        object_id: The ID of the Stories
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = Stories(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_insights_for_stories(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Insights for Stories.

    Args:
        object_id: The ID of the Stories
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights result
    """
    result = Stories(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


# Export the server
stories_server = mcp
