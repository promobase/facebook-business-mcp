"""
Auto-generated MCP server for Facebook IGMediaForIGOnlyAPI.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igmediaforigonlyapi import IGMediaForIGOnlyAPI
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-igmediaforigonlyapi")


# CRUD Operations


@mcp.tool()
async def get_igmediaforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a IGMediaForIGOnlyAPI.

    Args:
        object_id: The ID of the IGMediaForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = IGMediaForIGOnlyAPI(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_igmediaforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a IGMediaForIGOnlyAPI.

    Args:
        object_id: The ID of the IGMediaForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = IGMediaForIGOnlyAPI(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_comment_for_igmediaforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Comment for IGMediaForIGOnlyAPI.

    Args:
        object_id: The ID of the IGMediaForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_comment result
    """
    result = IGMediaForIGOnlyAPI(fbid=object_id).create_comment(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_children_for_igmediaforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Children for IGMediaForIGOnlyAPI.

    Args:
        object_id: The ID of the IGMediaForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_children result
    """
    result = IGMediaForIGOnlyAPI(fbid=object_id).get_children(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_comments_for_igmediaforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Comments for IGMediaForIGOnlyAPI.

    Args:
        object_id: The ID of the IGMediaForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_comments result
    """
    result = IGMediaForIGOnlyAPI(fbid=object_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_insights_for_igmediaforigonlyapi(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Insights for IGMediaForIGOnlyAPI.

    Args:
        object_id: The ID of the IGMediaForIGOnlyAPI
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_insights result
    """
    result = IGMediaForIGOnlyAPI(fbid=object_id).get_insights(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igmediaforigonlyapi_server = mcp
