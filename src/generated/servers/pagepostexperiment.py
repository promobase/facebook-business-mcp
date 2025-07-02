"""
Auto-generated MCP server for Facebook PagePostExperiment.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.pagepostexperiment import PagePostExperiment
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-pagepostexperiment")


# CRUD Operations


@mcp.tool()
async def delete_pagepostexperiment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a PagePostExperiment.

    Args:
        object_id: The ID of the PagePostExperiment
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = PagePostExperiment(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_pagepostexperiment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a PagePostExperiment.

    Args:
        object_id: The ID of the PagePostExperiment
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = PagePostExperiment(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def get_video_insights_for_pagepostexperiment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Video Insights for PagePostExperiment.

    Args:
        object_id: The ID of the PagePostExperiment
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_video_insights result
    """
    result = PagePostExperiment(fbid=object_id).get_video_insights(
        fields=fields,
        params=params,
    )

    return result


# Export the server
pagepostexperiment_server = mcp
