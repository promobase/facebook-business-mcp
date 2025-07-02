"""
Auto-generated MCP server for Facebook IGComment.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.igcomment import IGComment
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-igcomment")


# CRUD Operations


@mcp.tool()
async def delete_igcomment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a IGComment.

    Args:
        object_id: The ID of the IGComment
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = IGComment(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_igcomment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a IGComment.

    Args:
        object_id: The ID of the IGComment
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = IGComment(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_igcomment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a IGComment.

    Args:
        object_id: The ID of the IGComment
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = IGComment(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_reply_for_igcomment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Reply for IGComment.

    Args:
        object_id: The ID of the IGComment
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_reply result
    """
    result = IGComment(fbid=object_id).create_reply(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_replies_for_igcomment(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Replies for IGComment.

    Args:
        object_id: The ID of the IGComment
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_replies result
    """
    result = IGComment(fbid=object_id).get_replies(
        fields=fields,
        params=params,
    )

    return result


# Export the server
igcomment_server = mcp
