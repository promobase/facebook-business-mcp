"""
Auto-generated MCP server for Facebook LiveVideo.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.livevideo import LiveVideo
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-livevideo")


# CRUD Operations


@mcp.tool()
async def delete_livevideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete a LiveVideo.

    Args:
        object_id: The ID of the LiveVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete result
    """
    result = LiveVideo(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_livevideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a LiveVideo.

    Args:
        object_id: The ID of the LiveVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = LiveVideo(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_livevideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a LiveVideo.

    Args:
        object_id: The ID of the LiveVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = LiveVideo(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_input_stream_for_livevideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Input Stream for LiveVideo.

    Args:
        object_id: The ID of the LiveVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_input_stream result
    """
    result = LiveVideo(fbid=object_id).create_input_stream(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_poll_for_livevideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Poll for LiveVideo.

    Args:
        object_id: The ID of the LiveVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_poll result
    """
    result = LiveVideo(fbid=object_id).create_poll(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_blocked_users_for_livevideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Blocked Users for LiveVideo.

    Args:
        object_id: The ID of the LiveVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_blocked_users result
    """
    result = LiveVideo(fbid=object_id).get_blocked_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_comments_for_livevideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Comments for LiveVideo.

    Args:
        object_id: The ID of the LiveVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_comments result
    """
    result = LiveVideo(fbid=object_id).get_comments(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_crosspost_shared_pages_for_livevideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Crosspost Shared Pages for LiveVideo.

    Args:
        object_id: The ID of the LiveVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_crosspost_shared_pages result
    """
    result = LiveVideo(fbid=object_id).get_crosspost_shared_pages(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_crossposted_broadcasts_for_livevideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Crossposted Broadcasts for LiveVideo.

    Args:
        object_id: The ID of the LiveVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_crossposted_broadcasts result
    """
    result = LiveVideo(fbid=object_id).get_crossposted_broadcasts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_errors_for_livevideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Errors for LiveVideo.

    Args:
        object_id: The ID of the LiveVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_errors result
    """
    result = LiveVideo(fbid=object_id).get_errors(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_polls_for_livevideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Polls for LiveVideo.

    Args:
        object_id: The ID of the LiveVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_polls result
    """
    result = LiveVideo(fbid=object_id).get_polls(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_reactions_for_livevideo(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Reactions for LiveVideo.

    Args:
        object_id: The ID of the LiveVideo
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_reactions result
    """
    result = LiveVideo(fbid=object_id).get_reactions(
        fields=fields,
        params=params,
    )

    return result


# Export the server
livevideo_server = mcp
